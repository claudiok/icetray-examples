#!/usr/bin/env python

def main():
    """
    Note that this cpp service passes as easily to python modules as it does to
    c++ modules.
    """
    import sys

    from icecube import icetray, dataclasses, phys_services

    try:
        from icecube.examples.modules import UseRandom
    except ImportError:
        sys.exit(0)

    from I3Tray import I3Tray
    from os.path import expandvars

    rndserv = phys_services.I3GSLRandomService(31334)

    tray = I3Tray()

    tray.AddModule("BottomlessSource", "bs")

    tray.AddModule(UseRandom, "ur",
                   I3RandomService = rndserv,
                   PutWhere = "here")

    def showvalue(frame):
        d = frame.Get("here")
        print "Value is", d.value

    tray.AddModule(showvalue, "sv")

    tray.AddModule("TrashCan", "tc")

    tray.Execute(100)
    tray.Finish()

if __name__ == '__main__':
    main()
