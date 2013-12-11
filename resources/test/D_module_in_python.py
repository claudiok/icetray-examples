#!/usr/bin/env python

def main():
    """
    Simple module implementation in python.  
    """

    from icecube.icetray import I3Int, I3Module
    from I3Tray import I3Tray

    tray = I3Tray()

    # generate empty frames
    tray.AddModule("BottomlessSource","bottomless")


    class IntAdder(I3Module):
        def __init__(self, context):
            I3Module.__init__(self, context)
            self.AddParameter("value", "value of added int", 3)
            self.AddParameter("where", "where to put it", "i3int")
            self.AddOutBox("OutBox")

        def Configure(self):
            self.intval = self.GetParameter("value")
            self.where = self.GetParameter("where")

        def Physics(self, frame):
            i = I3Int(self.intval)
            frame.Put(self.where, i)
            self.PushFrame(frame)
            print(">>>>>>>>>> PyPhysics, frame has keys: %s" % (list(frame.keys())))

    tray.AddModule(IntAdder, "mod",
                   value = 17,
                   where = "steen")

    tray.AddModule("Dump","dump")

    tray.AddModule("TrashCan","adios")

    tray.Execute(6)

    # see ya.
    tray.Finish()

if __name__ == '__main__':
    main()
    
