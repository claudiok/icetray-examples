#!/usr/bin/env python
#
# Pass 7:
#
# Configuring a Module
#
# Module HelloConfigurations and this steering file demonstrate the
# range of ways to configure an I3Module.  This includes the usual
# POD's (Plain Old Data types, like bool, int, double and string) as
# well as OMKeys, and even vectors of ints, doubles and OMKeys.
#
# See the HelloConfigurations (both the .cxx and .h files) Module for
# how things look on the C++ side.  The python syntax is demonstrated
# below.
#
# After you run this script, pull up the .i3 file and hit 'c' to see
# the configuration.  Notice what the vectors of OMKeys and PODs look
# like.
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

#
# Default configuration of the I3Reader.  It
# doesn't really matter much as we're only going to run a couple of
# events and ignore the contents.
#
tray.AddModule("I3Reader","i3reader")(
    ("Filename", "pass1.i3"),
    )

#
# module exercises the configuration mechanisms.
#
tray.AddModule("HelloConfiguration", "configs")(
    ("mtgs/yr", 8),
    ("naps", True),
    ("COG", OMKey(13,13)),
    ("PeekFactor", 0.1234567890123456),
    ("Rather", "Uhm..."),
    ("vector_of_ints", [1,2,3,4,5,6,7,8,9] ),
    ("vector_of_ulongs", [256109,256110,256111,256112] ),
    ("vector_of_doubles", [0.1, 0.2, 0.3, 0.4, NaN, +Inf, -Inf, 4.18709e-11, 0.9]),
    ("vector_of_omkeys", [OMKey(1,1), OMKey(2,2), OMKey(3,3)] ),
    ("vector_of_strings", ["notice that", "this", "list",
                           "may contain",
                           " leading", "trailing ",
                           " and embedded whitespace\n"])
    )

tray.AddModule("I3Writer","writer")(
    ("filename", "HelloConfiguration.i3")
    )

tray.AddModule("Dump","dump")
tray.AddModule("TrashCan","tschuessi")

tray.Execute(1)
tray.Finish()
