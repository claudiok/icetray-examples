#!/usr/bin/env python
#
# Demonstrates the use of the "Smear" module to `smear' particles by
# a constant.
#

from I3Tray import *

from os.path import expandvars

import os
import sys

from icecube import icetray 
from icecube import dataclasses 
from icecube import phys_services 
from icecube import dataio 
from icecube import examples 

tray = I3Tray()

tray.AddModule("I3Reader","i3reader",
               Filename = "pass4.i3",
               SkipKeys = ["llh.*", "mutineer"]
               )

tray.AddService("I3GSLRandomServiceFactory", "random")

tray.AddModule("PutParticle", "putter",
               Zenith = 0,
               Azimuth = 0,
               Where = "zero_particle"
               )

tray.AddModule("Smear", "smear",
               Src = "zero_particle",
               Dst =  "smeared_particle",
               Mean = 0.0,
               Constant = 0.0,
               Sigma = 0.5
               )
    
tray.AddModule("I3Writer", "writer",
               filename = "smeared.i3"
               )

tray.AddModule("TrashCan","see_yas")

# run a bunch of events so the histograms look right.  Leave out the
# "dump" so as not to generate too much spew.
tray.Execute(1000)
tray.Finish()
