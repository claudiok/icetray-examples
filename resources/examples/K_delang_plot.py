#!/usr/bin/env python

def main():
    """
    Module makes a regularly updating 'DeltaAngle' plot

    Run like this::

      ipython -pylab K_delang_plot.py /path/to/file.i3

    you need ipython's threading to see it update in 'realtime'.  

    """

    from icecube import icetray, dataclasses, dataio, phys_services

    from I3Tray import I3Tray
    from os.path import expandvars
    import sys

    try:
        from icecube.examples.modules import DeltaAngle
    except ImportError:
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Usage:  %s somefile.i3" % sys.argv[0])
        sys.exit(0)

    tray = I3Tray()

    tray.AddModule("I3Reader", "drd",
                   Filename = sys.argv[1])

    tray.AddModule(DeltaAngle, "da",
                   lhs="IcLinefit",
                   rhs="TrackLlhFit")

    tray.AddModule("TrashCan", "tc")

    tray.Execute(100000)
    tray.Finish()




if __name__ == "__main__":
    main()
