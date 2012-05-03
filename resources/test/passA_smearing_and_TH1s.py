#!/usr/bin/env python
#
#
# Again calculating delta-angle, this time with *two* smearers and
# histogrammers.  Demonstrates that when modules are constructed
# "modularly" (small with well-defined responsibilities), you get
# extra degrees of freedom.
# 

from I3Tray import *

from os.path import expandvars

import os
import sys

from icecube import icetray 
from icecube import dataclasses 
from icecube import phys_services 
from icecube import examples 
from icecube import dataio 
from icecube import examples 

tray = I3Tray()

tray.AddService("I3GSLRandomServiceFactory", "randalicious")

tray.AddModule("I3Reader","i3reader",
               Filename = "pass4.i3",
               SkipKeys = [".*Result", "mutineer"]
               )

tray.AddModule("PutParticle", "putter",
               Zenith = 0,
               Azimuth = 0,
               Where = "zero_particle"
               )

tray.AddModule("Smear", "smear",
               Src = "zero_particle",
               Dst = "smeared_0.2",
               Mean = 0.0,
               Sigma = 0.2
               )
    
# rather strange smear
tray.AddModule("Smear", "smear2",
               Src = "zero_particle",
               Dst = "smeared_1.0",
               Mean = 0,
               Sigma = 1.0
               )
    
#
# Comparing two recos because there's no MC handy.
# Still have to figger the units with this.
#
tray.AddModule("DeltaAngle", "delta",
               lhs = "zero_particle",
               rhs = "smeared_0.2",
               th1_fname = "smeared.root"
               )

tray.AddModule("DeltaAngle", "delta2",
               lhs = "zero_particle",
               rhs = "smeared_1.0",
               th1_fname = "smeared.root"
               )

tray.AddModule("I3Writer", "writer",
               filename = "smeared.i3"
               )

tray.AddModule("TrashCan","see_yas")

# run a bunch of events so the histograms look right.  Leave out the
# "dump" so as not to generate too much spew.
tray.Execute(1000)
tray.Finish()
