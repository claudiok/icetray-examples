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
tray.AddService("OnlyOneModuleFibonacciServiceFactory", "fibi")(
    ("modulename", "sees_fib"),
    ("servicename", "where_it_sees_it")
    )

tray.AddModule("BottomlessSource","bottomless")

#
# unlike the previous script, this one succeeds since the factory above gives
# every module its own service.
#
tray.AddModule("FibonacciCheck", "check")

tray.AddModule("TrashCan","see_yas")

try:
    tray.Execute(30)
    tray.Finish()
except:
    sys.exit(0)
else:
    sys.exit(1)


