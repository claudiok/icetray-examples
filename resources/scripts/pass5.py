#!/usr/bin/env python
#
# Pass 5:
#
# In the last pass the MutineerModule put a track into the frame.  If
# we don't have the code for that module, its output is opaque to us.
# We can create that situation by simply not loading libmutineer.  Run
# this script as is, and observe that it runs to but that the MutineerTrack
# is not present in the frames as they come by.  We have told the 
# reader to skip any frame elements with the name 'mutineer' so it never
# even attempts to de-serialize those objects.
#
# You can make the script generate an error by commenting out the 
# 'SkipKeys' parameter to the ReaderSericeFactory.  You should then gen
# an error:
#
#   RuntimeError: Exception unregistered class loading class type
#   "MutineerTrack" at frame key "mutineer"
#
# Notice also that the I3Writer has a SkipKeys argument.  Since we're
# not interested in the IceTop data at the moment, we can tell the
# I3Writer to skip those keys when writing.
#
# Go have a look at the file with the dataio-shovel.  The mutineer
# tracks should be missing as well as the IceTop data.
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

tray.AddModule("I3Reader","reader")(
    ("Filename", "pass4.i3"),
    ("SkipKeys", ["mutineer"])
    )

tray.AddModule("I3Writer","writer")(
    ("filename", "pass5.i3"),
    ("SkipKeys", ["IceTopRawData", "IceTopRecoHitSeries"])
    )

# the usual Dump -> Trash
tray.AddModule("Dump","dump")
tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()
