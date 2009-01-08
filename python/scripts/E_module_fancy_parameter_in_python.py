#!/usr/bin/env python

def main():
    """
    You can pass arbitrary python objects to python-I3Modules through their parameters
    """

    from icecube.icetray import I3Module, I3Int
    from I3Tray import I3Tray

    tray = I3Tray()

    # generate empty frames
    tray.AddModule("BottomlessSource","bottomless")

    class MultiAdder(I3Module):
        def __init__(self, context):
            I3Module.__init__(self, context)
            self.AddParameter("values", "key/value pairs to put into the frame", None)

        def Configure(self):
            self.d = self.GetParameter("values")
            print ">>>>> Configured with", self.d

        def Physics(self, frame):
            for (k,v) in self.d.items():
                i = I3Int(v)
                frame.Put(k, i)
            self.PushFrame(frame)

    tray.AddModule(MultiAdder, "mod",
                   values = { 'one' : 1,
                              'two' : 2,
                              'three' : 777 })

    tray.AddModule("Dump","dump")

    tray.AddModule("TrashCan","adios")

    tray.Execute(6)

    tray.Finish()

if __name__ == "__main__":
    main()
