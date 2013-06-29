from icecube import icetray
from icecube.util import delta_angle
import pylab,numpy

class DeltaAngle(icetray.I3Module):
    """
    Module calculates the delta angle of two particles in the frame and
    Pops up a histogram every 500 events.

    *Parameters*:

    * **lhs** - left-hand particle name
    * **rhs** - right-hand particle name

    Example::

      tray.AddModule(examples.DeltaAngle, 'de',
                     lhs = 'linefit',
                     rhs = 'megafit')

    .. warning::

       You must run this under ``ipython -pylab`` or the script will not
       autoupdate, the plot's event loop will hang the script.

    """
    def __init__(self, context):
        pylab.hold(False)
        icetray.I3Module.__init__(self, context)
        self.AddOutBox("OutBox")
        self.data = []
        self.nevents = 0
        self.AddParameter("lhs", "lefthand-particle", "")
        self.AddParameter("rhs", "righthand-particle", "")
        
    def Configure(self):
        self.lhsname = self.GetParameter("lhs")
        self.rhsname = self.GetParameter("rhs")
        
    def Physics(self, frame):
        lhparticle = frame.Get(self.lhsname)
        rhparticle = frame.Get(self.rhsname)

        self.nevents += 1
        da = delta_angle(lhparticle, rhparticle)*180./numpy.pi
        if da:
            self.data.append(da)

        if self.nevents % 500 == 0:
            (data, bins) = numpy.histogram(self.data, bins=18, range=(0.,180.))
            pylab.plot(bins[:-1], data, linestyle='steps')
            pylab.savefig("delta%06d.png" % self.nevents)
            print(">> %d" % self.nevents)
