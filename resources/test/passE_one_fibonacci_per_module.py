#!/usr/bin/env python
#
# This script uses the example "singleton fibonacci" service.  This
# points out that each 
#

from I3Tray import *

from os.path import expandvars

import os
import sys

from icecube import icetray 
from icecube import dataclasses 
from icecube import dataio 
from icecube import examples 

tray = I3Tray()


#
#  
#
tray.AddService("OnePerModuleFibonacciServiceFactory", "fibi")

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

tray.Execute(30)
tray.Finish()
