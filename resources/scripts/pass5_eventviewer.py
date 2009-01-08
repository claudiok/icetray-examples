#!/usr/bin/env python
#
# Pass 5_eventviewer:
#
#  The event viewer!  Lets view your pass5.i3 file in the event viewer!
#    It just reads, doesn't write anything


import os
import sys
from os.path import expandvars

print "This script uses X11... please delete this line and the one following to use."
sys.exit(0)

from I3Tray import *

load("libicetray")
load("libdataclasses")
load("libdataio")
load("libexamples")  # hello world is in there
load("libeventviewer")

tray = I3Tray()

#
# Default configuration of the I3Muxer and the I3ReaderServices. 
#
tray.AddModule("I3Reader","i3reader")(
    ("Filename", "pass4.i3"),
    ("SkipKeys", ["mutineer"]),
    )

tray.AddModule("I3Muxer","muxer")

#
# Gimme an event viewer!
#
tray.AddModule("I3EventViewerModule", "theviewer")(
    )

tray.AddModule("Dump","dump")
tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()
