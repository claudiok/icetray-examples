#!/usr/bin/env python

def main():
    """
    Pass a function that has some 'state' to I3Tray by using a closure
    """

    from icecube.icetray import I3Int
    from I3Tray import I3Tray

    tray = I3Tray()

    def putints(startwith):
        putints.n = startwith
        def f(frame):
            i = I3Int(putints.n)
            d = frame.Put("sevenseven", i)
            putints.n += 1
        return f



    tray.AddModule("BottomlessSource", "bs")

    tray.AddModule(putints(13), "sv")

    def showint(whichint):
        showint.name = whichint
        def f(frame):
            i = frame.Get(showint.name)
            print ">>>> I3Int @ ", showint.name, "==", i.value, "<<<<"
        return f


    tray.AddModule(showint("sevenseven"), "si")
    tray.AddModule("Dump", "dmp")

    tray.AddModule("TrashCan", "trash")

    tray.Execute(4)

    tray.Finish()

if __name__ == "__main__":
    main()
