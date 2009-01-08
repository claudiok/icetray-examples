from icecube import icetray
from icecube.util import delta_angle
import pylab

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
        da = delta_angle(lhparticle, rhparticle)
        if da:
            self.data.append(da)

        if self.nevents % 500 == 0:
            (data, bins) = numpy.histogram(self.data, 50)
            pylab.plot(bins, data, linestyle='steps')
            print ">>", self.nevents
            
