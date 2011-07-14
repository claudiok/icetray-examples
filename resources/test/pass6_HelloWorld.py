#!/usr/bin/env python
#
# Pass 6:
#
# Writing your own module:  HelloWorld!
#
# It is Hello World time.  That's right.  Hello World is in examples.
# It takes an I3String (a string that can live in the frame), sets the
# value as instructed and puts the ubiquitous greeting in the frame,
# where you can see it go by in the Dump as the script runs, or look
# at it in XML in the .i3 file with the dataio-shovel.
#

from I3Tray import *

from os.path import expandvars

import os
import sys

load("libicetray")
load("libdataclasses")
load("libdataio")
load("libexamples")  # hello world is in there

tray = I3Tray()

#
# Default configuration of the I3Reader
#
tray.AddModule("I3Reader","i3reader",
               Filename = "pass1.i3",
               )

#
# Aloha Honolulu!
#
tray.AddModule("HelloWorld", "hello",
               Where = "Honolulu",
               SayWhat = "Aloha"
               )

#
# Default I3Writer/Dump/Trash configuration
#
tray.AddModule("I3Writer","writer",
               filename = "pass6.i3",
               )

tray.AddModule("Dump","dump")
tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()
