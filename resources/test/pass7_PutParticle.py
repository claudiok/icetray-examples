#!/usr/bin/env python
#
# Check out the code for "PutParticle", which creates an I3Particle
# with some values and puts it in the frame.  Later on we'll copy and
# jiggle those around and make delta-angle histograms.
#

from I3Tray import *

from os.path import expandvars

import os
import sys

from icecube import icetray 
from icecube import dataclasses 
from icecube import dataio 
from icecube import examples 

tray = I3Tray()

#
# Default configuration of the I3Reader
#
tray.AddModule("I3Reader","i3reader",
               Filename = "pass1.i3"
               )

#
# The parameter names here should be pretty self-explanatory.  The
# particles get distinctive values for zen/azi so you can have a look
# at the XML and see that the data got through to the .i3 file.
#
tray.AddModule("PutParticle", "putter",
               Zenith = 1.010101,
               Azimuth = 2.020202,
               Where = "zero_particle"
               )

tray.AddModule("I3Writer", "writer",
               filename = "pass7_PutParticle.i3"
               )

tray.AddModule("TrashCan", "later")

tray.Execute()
tray.Finish()
