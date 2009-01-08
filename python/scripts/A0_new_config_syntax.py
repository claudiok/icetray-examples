#!/usr/bin/env python

def main():
    """
    Demonstrates new keyword-configuration syntax of tray.
    """
    from icecube.icetray import I3Int
    from I3Tray import I3Tray

    tray = I3Tray()

    def showvalue(frame):
        d = frame.Put("sevenseven", I3Int(777))

    tray.AddModule("BottomlessSource", "bs")

    tray.AddModule("AddNulls", "an",
                   where = ["here", "there", "everywhere"])

    tray.AddModule("Copy", "cpy",
                   Keys = ["here", "here2",
                           "there", "there2"])

    tray.AddModule("CountFrames", "cf",
                   Physics = 17,
                   Geometry = 0,
                   Calibration = 0,
                   DetectorStatus = 0)

    tray.AddModule("CountObject", "co",
                   expected=17,
                   where="here2")

    tray.AddModule("Dump", "dmp")

    tray.AddModule("TrashCan", "trash")

    tray.Execute(17)

    tray.Finish()


if __name__ == '__main__':
    main()
