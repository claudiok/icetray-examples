#!/usr/bin/env python

from icecube import icetray, dataclasses, dataio

class GThenEmptyPhysics(icetray.I3Module):
    """
    Source module that reads GCD from an i3 file, then pushes empty
    physics frames.
    """
    def __init__(self, context):
        icetray.I3Module.__init__(self, context)
        self.AddParameter('GCD', 'Where to get gcd from', None)
        self.AddOutBox('OutBox')

    def Configure(self):
        fname = self.GetParameter('GCD')
        print("opening %s" % fname)
        self.i3f = dataio.I3File(fname)
        
    def Process(self):
        fr = self.i3f.pop_frame(icetray.I3Frame.Geometry)
        print(fr)
        if not fr:
            fr = icetray.I3Frame(icetray.I3Frame.Physics)

        self.PushFrame(fr)

