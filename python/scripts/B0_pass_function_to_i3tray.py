#!/usr/bin/env python

def main():
    """
    Pass a simple function to I3Tray.AddModule()
    """

    from icecube.icetray import I3Int
    from I3Tray import I3Tray

    tray = I3Tray()

    #
    #  Python function that takes a frame and puts an I3Int in it.
    #
    def putsomething(frame):
        d = frame.Put("sevenseven", I3Int(777))

    tray.AddModule("BottomlessSource", "bs")

    #
    #  You pass a function object to AddModule... a special I3Module
    #  of type PythonFunction gets created that calls the python function
    #  on every frame.  Frames get pushed to the one outbox "OutBox"
    #  if the function returns True (or doesn't return anything, i.e. None).
    #  If the function returns False the frame will be dropped.
    #
    tray.AddModule(putsomething, "sv")

    tray.AddModule("Dump", "dmp")

    tray.AddModule("TrashCan", "trash")

    tray.Execute(4)

    tray.Finish()

if __name__ == "__main__":
    main()
