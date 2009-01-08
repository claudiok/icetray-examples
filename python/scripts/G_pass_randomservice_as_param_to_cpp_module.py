#!/usr/bin/env python

def main():
    """
    Pass a randomservice as a parameter to a module...  no servicefactories needed.
    """

    from icecube import icetray, dataclasses, phys_services, examples
    from I3Tray import I3Tray

    rndserv = phys_services.I3GSLRandomService(31334)

    tray = I3Tray()

    tray.AddModule("BottomlessSource", "bs")

    #
    #  Module 'UseRandom' gets a I3RandomServicePtr
    #  as a parameter... the derived type (here, I3GSLRandomService)
    #  is hidden from the module.  As it should be.
    # 
    tray.AddModule("UseRandom", "ur",
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
