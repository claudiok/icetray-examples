#!/usr/bin/env python
#
# Pass 4:
#
# Here we make another pass at the data and this time do a
# reconstruction with a minimzer.  We also use the "mutineer" project
# to put an object in the frame that we will later filter out: this is
# to demonstrate how to keep data you can't read from getting in your
# way.
#

from I3Tray import *

from os.path import expandvars

import os
import sys

from icecube import icetray 
from icecube import dataclasses 
from icecube import dataio 
from icecube import examples 
from icecube import mutineer 

tray = I3Tray()

# The reader
tray.AddModule("I3Reader","reader",
               Filename = "pass1.i3"
               )

# The Mutineer module just puts things in the frame that we dont have
# code for.  We filter this thing out later.
tray.AddModule("MutineerModule", "arrr")

# Write the data with our new reconstruction.  Same usage of the
# writer as in pass1.
tray.AddModule("I3Writer","writer",
               filename =  "pass4.i3"
               )

#
# This is the usual Dump + TrashCan idiom at the end.  Watch for the
# MutineerTracks and the new reconstruction alongside its seeds.
#
tray.AddModule("Dump","dump")
tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()
