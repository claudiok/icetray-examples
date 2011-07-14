#!/usr/bin/env python
#
# Pass 9:
#
# Calculating delta-angle
#
# Generate histograms of delta angle on dummy "smeared" data.
#

from I3Tray import *

from os.path import expandvars

import os
import sys

load("libicetray")
load("libdataclasses")
load("libdataio")
load("libexamples") 

tray = I3Tray()

tray.AddService("I3SPRNGRandomServiceFactory", "random")

tray.AddModule("I3Reader","i3reader",
               Filename = "pass1.i3",
               )

tray.AddModule("PutParticle", "putter",
               Zenith = 3.14159,
               Azimuth = 2.010101,
               Where = "zero_particle"
               )

tray.AddModule("Smear", "smear",
               Src = "zero_particle",
               Dst = "smeared_particle",
               Constant = 0,
               Mean = 0,
               Sigma = 0.5
               )
    
#
# Comparing the angles and dump a root file containing a TH1
#
tray.AddModule("DeltaAngle", "delta",
               lhs = "zero_particle",
               rhs = "smeared_particle",
               th1_fname = "pass9_DeltaAngle.root"
               )

tray.AddModule("I3Writer", "writer",
               filename = "smeared.i3"
               )

tray.AddModule("TrashCan","see_yas")

# run a bunch of events so the histograms look right.  Leave out the
# "dump" so as not to generate too much spew.
tray.Execute(1000)
tray.Finish()
