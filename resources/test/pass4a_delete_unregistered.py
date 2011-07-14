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

load("libicetray")
load("libdataclasses")
load("libdataio")

tray = I3Tray()

# The reader
tray.AddModule("I3Reader","reader",
               Filename =  "pass4.i3"
               )

# This should skip things that aren't registered... specifically the mutineer
# code for.  We filter this thing out later.
tray.AddModule("DeleteUnregistered", "deleter")

# verify that it was skipped
tray.AddModule("FrameCheck", "checker",
               Ensure_Physics_Hasnt =  ["mutineer"]
               )

tray.AddModule("Dump","dump")

tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()
