#!/usr/bin/env python

from icecube import icetray, dataclasses

import os

import numpy as n

def sph2car(fromz, aroundz, r):
    """
    convert spherical to cartesian coordinates.

    'fromz' == 'theta', 'aroundz' == 'phi'

    """
    return n.array([n.sin(fromz) * n.cos(aroundz),
                    n.sin(fromz) * n.sin(aroundz),
                    n.cos(fromz)]) * r

class ThroughgoingTrack(icetray.I3Module):
    """
    A simmish example module that makes a bunch of hits that look
    Cherenkovlike and adds the particle that could have produced them.
    """

    def __init__(self, context):
        icetray.I3Module.__init__(self, context)
        self.AddParameter('hits_outname', 'where to put the hits', 'InIceRecoHitSeries')
        self.AddParameter('particle_outname', 'where to put the particle', 'mctrack')
        self.AddParameter('rand', 'an I3RandomService', None)
        self.AddOutBox('OutBox')
        
    def Configure(self):
        self.rand = self.GetParameter('rand')
        self.hits_whereto = self.GetParameter('hits_outname')
        self.particle_whereto = self.GetParameter('particle_outname')

    def Geometry(self, frame):
        self.omgeo = frame['I3Geometry'].omgeo
        z_positions = [entry.data().position.Z for entry in self.omgeo
                         if entry.data().omtype != dataclasses.I3OMGeo.OMType.IceTop]
        self.minz = min(z_positions)
        self.maxz = max(z_positions)
        self.mygeo = dict([(entry.key(), n.array([entry.data().position.X,
                                                  entry.data().position.Y,
                                                  entry.data().position.Z]))
                           for entry in self.omgeo
                           if entry.data().omtype != dataclasses.I3OMGeo.OMType.IceTop])

        self.PushFrame(frame)
        
    @staticmethod
    def is_inside(point, conetip, conedirection, coneangle):
        # v1: normalized particle direction vector
        v1 = conedirection / n.sqrt(n.sum(conedirection*conedirection)) 

        # uv2: unnormalized vector from tip of cone to point
        uv2 = (conetip - point)
        # v2: normalized vector from tip of cone to point
        v2 = uv2 / n.sqrt(n.sum(uv2*uv2)) 

        theta = n.arccos(n.dot(v1, v2))
        return theta < coneangle

    def Physics(self, frame):

        initpos = n.array([0,  0, self.minz-10])
        theta, phi, r = (0.25, 0.07, dataclasses.I3Constants.c)

        #
        # Create and put the particle responsible for the hits we're
        # about to generate
        #
        p = dataclasses.I3Particle()
        p.SetThetaPhi(theta, phi)
        p.SetPos(*initpos)
        p.SetTime(0)
        frame[self.particle_whereto] = p

        hits = dataclasses.I3RecoHitSeriesMap()
        direction = sph2car(theta, phi, r)
        print direction

        times = n.linspace(0, 40000, 100)

        for t in times:
            print t, '\r'
            newpos = initpos + (t * direction)

            for (omkey, ompos) in self.mygeo.iteritems():

                if omkey in hits:
                    continue

                dist = n.sqrt(n.sum((ompos - newpos) * (ompos-newpos)))

                if dist > 350:
                    continue

                if self.__class__.is_inside(point=ompos,
                                            conetip=newpos,
                                            conedirection=direction,
                                            coneangle=dataclasses.I3Constants.theta_cherenkov):

                    hit = dataclasses.I3RecoHit()
                    hit.Time = t
                    vh = dataclasses.vector_I3RecoHit()
                    vh.append(hit)
                    hits[omkey] = vh

        frame[self.hits_whereto] = hits
        self.PushFrame(frame)

