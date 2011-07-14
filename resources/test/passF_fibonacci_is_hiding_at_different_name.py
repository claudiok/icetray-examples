#!/usr/bin/env python
#
# This script uses the example "singleton fibonacci" service.  This
# points out that each 
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
#  
#
tray.AddService("NamedFibonacciServiceFactory", "fibi",
                name = "fibonacci_aside"
                )

tray.AddModule("BottomlessSource","bottomless")

#
# unlike the previous script, this one succeeds since the factory above gives
# every module its own service.
#
tray.AddModule("FibonacciCheck", "check1")
tray.AddModule("FibonacciCheck", "check2")
tray.AddModule("FibonacciCheck", "check3")
tray.AddModule("FibonacciCheck", "check4")

tray.AddModule("TrashCan","see_yas")

try: 
    tray.Execute(30)
    tray.Finish()
except:
    print "Tray failed as it should have"
    sys.exit(0)
else:
    sys.exit(1)


