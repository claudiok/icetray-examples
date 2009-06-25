#!/usr/bin/env python
#
#
# Pass 1: this does a first pass through the data and uses the Muxer
# to talks to the various messy services with complicated
# configurations and filesystem dependencies.  It generates
# "pass1.i3", a platform-independent datafile that you can read with
# just a few lines of configuration (see pass2.py...)
#

from I3Tray import *

from os.path import expandvars

import os
import sys

load("libicetray")
load("libdataclasses")
load("libphys-services")
load("libDOMcalibrator")
load("libdataio")
load("libexamples")

#
# This sets up a bunch of paths of files and stuff.  Nice to have a
# real scripting language at one's disposal for this kind of thing.
#
tools = expandvars("$I3_PORTS")
runfile = tools + "/test-data/2006data/Run00089508.i3.gz"

#
#  The services that provide data to the I3Muxer (multiplexer).
#
tray = I3Tray()

tray.AddModule("I3Reader","i3reader")(
    ("Filename", runfile),
    ("SkipKeys",["I3PfFilterMask"])
    )

#
# A DOMCalibrator.  Obviously.
#
tray.AddModule("I3DOMcalibrator","merge")
 
#
# And an appropriately named but nonetheless cute feature
# extractor.
#
tray.AddModule("DumbFeatureExtractor","dumbfe")
 
#
# This is the very convenient "Dump" module which spits out the frames
# as they go by.  This is one of icecube's standard modules (in
# project icetray.  You get it for free, it's always available.)
#
tray.AddModule("Dump","dump")

#
# And this is the magic writer.  We will make it work harder later.
#
tray.AddModule("I3Writer","writer")(
    ("filename", "pass1.i3")
    )

#
# The TrashCan is another standard module.  Every module's outboxes
# must be connected to something.  The I3Writer, above, sends things
# downstream after it has written them because it doesn't know if it
# really is going to be the last module in the chain.  This module
# catches whatever comes through and just discards it.
#
tray.AddModule("TrashCan", "the can");

#
# Here we specify how many frames to process, or we can omit the
# argument to Execute() and the the tray will run until a module tells
# it to stop (via RequestSuspension()).  We'll do a few frames so
# there's a chunk of data involved.
#
tray.Execute()
tray.Finish()
