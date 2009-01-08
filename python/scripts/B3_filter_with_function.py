#!/usr/bin/env python

def main():
    """
    Filter frames with a function
    """
    from icecube.icetray import I3Int
    from I3Tray import I3Tray

    tray = I3Tray()


    tray.AddModule("BottomlessSource", "bs")

    def putints(where, startwith):
        putints.where = where
        putints.n = startwith
        def f(frame):
            i = I3Int(putints.n)
            d = frame.Put(putints.where, i)
            putints.n += 1
        return f

    tray.AddModule(putints("sevenseven", 13), "sv")


    def filter(frame):
        i = frame.Get("sevenseven")
        val = i.value
        return val % 2 == 0

    tray.AddModule(filter, "filter")

    #
    # You can do the same thing as above, with a lambda function too:
    # tray.AddModule(lambda frame: frame.Get("sevenseven").value % 2 == 0, "filter")
    #

    def showint(whichint):
        showint.name = whichint
        def f(frame):
            i = frame.Get(showint.name)
            print ">>>> I3Int @ ", showint.name, "==", i.value, "<<<<"
        return f

    tray.AddModule(showint("sevenseven"), "si")


    tray.AddModule("TrashCan", "trash")

    tray.Execute(8)

    tray.Finish()

if __name__ == '__main__':
    main()
