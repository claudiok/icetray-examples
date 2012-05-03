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
tray.AddService("SingletonFibonacciServiceFactory", "fibi")

tray.AddModule("BottomlessSource","bottomless")

tray.AddModule("FibonacciCheck", "check")

tray.AddModule("TrashCan","see_yas")

tray.Execute(30)
tray.Finish()
