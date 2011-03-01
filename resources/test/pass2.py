#!/usr/bin/env python
#
# Pass 2:
#
# Now that we have a .i3 file, this is how small scripts get to do a
# simple pass through the data. It uses the I3Reader to load
# geometry/calibration/status/events into a running tray, dumps the
# frame to the console with the Dump, and puts them in the TrashCan.
#
# After this you should take a look at the pass1.i3 file with the
# dataio-shovel.  Check the dataio-shovel's help while you're there.
#

from I3Tray import *

from os.path import expandvars

import os
import sys

load("libicetray")
load("libdataio")

tray = I3Tray()

# The reader
tray.AddModule("I3Reader","reader")(
    ("Filename", "pass1.i3")
    )

# the dump shows you what's going by as it happens
tray.AddModule("Dump","dump")

# and the data disappears.  All the modules' boxes must be connected,
# so you need something here to catch the output from the Dump.  The
# TrashCan itself has no OutBox, as you might guess.
tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()
