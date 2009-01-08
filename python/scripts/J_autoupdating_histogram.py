#!/usr/bin/env python

def main():
    """
    Make an updating histogram. 

    Run like this: ipython -pylab this_script_name so you get
    nonblocking calls to pylab stuff.
    """

    from icecube import icetray, dataclasses, phys_services, examples

    from I3Tray import I3Tray
    from os.path import expandvars

    from pylab import plot, show, cla, hold

    import numpy

    rndserv = phys_services.I3GSLRandomService(31334)

    tray = I3Tray()

    tray.AddModule("BottomlessSource", "bs")

    tray.AddModule("UseRandom", "ur",
                   I3RandomService = rndserv,
                   PutWhere = "here")

    class Plotter(icetray.I3Module):
        def __init__(self, context):
            icetray.I3Module.__init__(self, context)
            self.data = []
            self.nevents = 0
            self.AddParameter("where", "", "")

        def Configure(self):
            self.where = self.GetParameter("where")
            hold(False)
            plot([])
            show()


        def Process(self):
            frame = self.PopFrame()
            thisdata = frame.Get(self.where).value
            self.nevents += 1
            self.data.append(thisdata)
            if self.nevents % 1500 == 0:
                (data, bins) = numpy.histogram(self.data, 50)
                plot(bins, data, linestyle='steps')
                print ">>", self.nevents

    tray.AddModule(Plotter, "plot",
                   where="here")

    tray.AddModule("TrashCan", "tc")

    tray.Execute(100000)
    tray.Finish()

if __name__ == "__main__":
    main()
