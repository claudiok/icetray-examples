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
tray.AddService("SingletonFibonacciServiceFactory", "fibi")

tray.AddModule("BottomlessSource","bottomless")

#
# these two fibonacci checkers will be talking to the same service and
# will get every-other fibonacci number.  Bad.
#
tray.AddModule("FibonacciCheck", "check1")
tray.AddModule("FibonacciCheck", "check2")

tray.AddModule("TrashCan","see_yas")

try:
    tray.Execute(30)
    tray.Finish()
except:
    print "Tray threw an exception as it should have"
    sys.exit(0)
else:
    sys.exit(1)
