#!/usr/bin/env python

def main():
    """
    Demonstrate passing a wrapped C++ object to an I3Module through its parameter
    """
    from icecube.icetray import I3Int
    from icecube import examples
    from I3Tray import I3Tray

    tray = I3Tray()

    i3int = I3Int(777)

    #
    # You can pass a frameobject to an I3Module.  The I3Module just does
    # I3IntPtr ip;
    # GetParameter("where", ip);
    #
    # Note the new keyword argument syntax
    #
    tray.AddModule("GetI3Int","giint",
                   obj = i3int)

    tray.AddModule("TrashCan", "trash")

    #
    # Doesn't actually do anything... just demonstrates that the I3Int
    # makes it through to The GetI3Int module
    #
    tray.Execute(1)

    tray.Finish()

if __name__ == '__main__':
    main()
    
