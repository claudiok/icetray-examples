#!/usr/bin/env python
#
# Sample Implementation of LineFit in python
#

from icecube.icetray import *
from icecube.dataclasses import *
import numpy

class LineFit(I3Module):
    def __init__(self, context):
        I3Module.__init__(self, context)
        self.AddParameter("AmpWeightPower", "Hits are weighted with the amplitude raised to this power."
                          "Typically 0. (for all hits weight=1) or 1. (weight=amplitude)", 
                          0)
        self.AddParameter("InputRecoHits", 
                          "RecoHitSeriesMap to use for input",
                          "InitialHitSeriesReco" )
        self.AddParameter("LeadingEdge", 
                          "True: Use the First hit per dom, False: Use all hits in the dom",
                          True)
        self.AddParameter("MinHits", 
                          "Minimum number of hits: events with fewer hits will not be reconstructed.",
                          2)
        self.AddParameter("Name", 
                          "Name to give the fit the module adds to the event",
                          "LineFit" )

        self.AddOutBox("OutBox")
        
    def Configure(self):
        self.AmpWeightPower=self.GetParameter("AmpWeightPower")
        self.InputRecoHits =self.GetParameter("InputRecoHits")
        self.LeadingEdge   =self.GetParameter("LeadingEdge")
        self.MinHits       =self.GetParameter("MinHits")
        self.Name          =self.GetParameter("Name")
        
    def Physics(self, frame):
        Geometry=frame.Get("I3Geometry").omgeo

        HitSeriesMap=frame.Get(self.InputRecoHits)

        particle=I3Particle();

        if not HitSeriesMap:
            particle.SetFitStatus(I3Particle.FitStatus.GeneralFailure)
        elif len(HitSeriesMap) < self.MinHits:
            particle.SetFitStatus(I3Particle.FitStatus.InsufficientHits)
        else:
            AverageTime        = 0
            AverageTimeSquared = 0
            AveragePosition    = numpy.zeros(3)
            AverageTimePosition= numpy.zeros(3)
            AmpSum             = 0
            for HitSeries in HitSeriesMap:
                position=Geometry[HitSeries.key()].position
                if self.LeadingEdge:
                    hits = HitSeries.data()[0:1]
                else:
                    hits = HitSeries.data() 
                for hit in hits:
                    time = hit.Time
                    try:
                        charge=hit.Charge
                    except:
                        charge=1
                    amp  = charge**self.AmpWeightPower
                    AmpSum            +=amp
                    AverageTime       +=amp*time
                    AverageTimeSquared+=amp*time**2
                    
                    array=numpy.array([position.X,position.Y,position.Z])
                    AveragePosition+=amp*array
                    AverageTimePosition+=amp*array*time
                        
            AverageTime        /=AmpSum
            AverageTimeSquared /=AmpSum
            AveragePosition    /=AmpSum
            AverageTimePosition/=AmpSum
            
            velocity=(AverageTimePosition-AveragePosition*AverageTime)/(AverageTimeSquared-AverageTime**2)

            particle.SetShape(I3Particle.ParticleShape.InfiniteTrack)
            particle.SetFitStatus(I3Particle.FitStatus.OK)
            particle.SetPos(AveragePosition[0],AveragePosition[1],AveragePosition[2])
            particle.SetDir(velocity[0],velocity[1],velocity[2])
            particle.SetTime(AverageTime)
            particle.SetSpeed(sum(velocity**2)**0.5)


        frame.Put(self.Name,particle)
        self.PushFrame(frame)


