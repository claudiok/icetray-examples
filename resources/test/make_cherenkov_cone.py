#!/usr/bin/env python

def main():
    """
    Use a couple of python modules to make a track-like set of hits in
    the detector.

    """

    from icecube import icetray, dataclasses, dataio, util
    from I3Tray import I3Tray
    from icecube.examples.modules import ThroughgoingTrack, GThenEmptyPhysics
    import os

    tray = I3Tray()

    tray.AddModule(GThenEmptyPhysics, 'src',
                   GCD = util.gcd)

    tray.AddModule("Dump", 'd')

    tray.AddModule(ThroughgoingTrack, 'mt',
                   hits_outname = 'InIceRecoHitSeries',
                   particle_outname = 'tracky')

    tray.AddModule('I3Writer', 'wr',
                   filename = 'out.i3')

    tray.AddModule('TrashCan', 'tc')
    tray.Execute(2)

    tray.Finish()

if __name__ == '__main__':
    main()
