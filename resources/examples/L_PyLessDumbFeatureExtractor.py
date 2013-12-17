#!/usr/bin/env python

def main():
    """
    Python implementation of the silly 
    """
    #
    #  Run C++ and python feature extractors in parallel
    #
    from icecube import util, icetray, dataclasses, dataio, examples

    from I3Tray import I3Tray

    tray = I3Tray()

    tray.AddModule("I3Reader","i3reader",
                   Filename = util.icdata_2007,
                   SkipKeys = ["CalibratedATWD", "CalibratedFADC"] # our FE will need these slots
                   )

    #
    # And an appropriately named but nonetheless cute feature
    # extractor.
    #
    tray.AddModule("LessDumbFeatureExtractor","lessdumbfe")

    #
    #  Same thing... but in python
    #
    import sys
    try:
        from icecube.examples.modules import LessDumbFeatureExtractor as PyLessDumbFeatureExtractor
    except ImportError:
        sys.exit(0)

    tray.AddModule(PyLessDumbFeatureExtractor, "pylessdumbfe",
                   Launches_in = "InIceRawData",
                   Hits_out = "pyhits",
                   Pulses_out = "pypulses")

    #
    # This is the very convenient "Dump" module which spits out the frames
    # as they go by.  This is one of icecube's standard modules (in
    # project icetray.  You get it for free, it's always available.)
    #
    tray.AddModule("Dump","dump")

    #
    # And this is the magic writer.  We will make it work harder later.
    #
    tray.AddModule("I3Writer","writer",
                   filename = "pyfe.i3"
                   )

    #
    # The TrashCan is another standard module.  Every module's outboxes
    # must be connected to something.  The I3Writer, above, sends things
    # downstream after it has written them because it doesn't know if it
    # really is going to be the last module in the chain.  This module
    # catches whatever comes through and just discards it.
    #
    tray.AddModule("TrashCan", "the can")

    #
    # Here we specify how many frames to process, or we can omit the
    # argument to Execute() and the the tray will run until a module tells
    # it to stop (via RequestSuspension()).  We'll do a few frames so
    # there's a chunk of data involved.
    #
    tray.Execute()
    tray.Finish()

if __name__ == '__main__':
    main()
