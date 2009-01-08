#!/usr/bin/env python

def main():
    """
    Implement a randomservice in python and pass it to a c++
    module... who really doesn't know whether he's talking to a cpp or
    a python randomservice.
    """

    from icecube import icetray, dataclasses, phys_services

    #
    # This is a python implementation of I3RandomService.  Services need a
    # special (but not so complicated) wrapper to be implementable in
    # python.   I3RandomService has such a wrapper.
    #
    from icecube.examples.services import ConstantService

    from I3Tray import I3Tray
    from os.path import expandvars

    rndserv = ConstantService(77767)

    tray = I3Tray()

    tray.AddModule("BottomlessSource", "bs")

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

"""
"""
if __name__ == "__main__":
    main()
