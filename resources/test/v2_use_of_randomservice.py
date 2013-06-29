#!/usr/bin/env python
#
# This script uses the example "singleton fibonacci" service.  This
# points out that each 
#

from icecube import icetray, dataclasses
from I3Tray import *

from os.path import expandvars

import os
import sys

from icecube import icetray 
from icecube import dataclasses 
from icecube import examples 
from icecube import phys_services 

tray = I3Tray()


#
#   Ask the tray to create an I3GSLRandomServiceFactory which
#   will in turn create a GSLRandomService and put it into the
#   context.  We don't know w/o looking at the code how many
#   it will create.
#
tray.AddService("I3GSLRandomServiceFactory", "servfactory",
                InstallServiceAs = "gslrandomserv",
                Seed = 31337
                )

tray.AddModule("BottomlessSource","bottomless")

#
# unlike the previous script, this one succeeds since the factory above gives
# every module its own service.
#
tray.AddModule("UseRandomV2", "userand",
               I3RandomServiceKey = "gslrandomserv",
               PutWhere = "randomdouble"
               )

def p(frame):
    print(frame)
    print(frame['randomdouble'].value)

tray.AddModule(p, 'p')

tray.AddModule("TrashCan","see_yas")

tray.Execute(30)


