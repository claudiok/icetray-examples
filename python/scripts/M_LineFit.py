#!/usr/bin/env python
#
# 
#

from I3Tray import *
from modules.LineFit import LineFit as PyLineFit 
from modules.LessDumbFeatureExtractor import LessDumbFeatureExtractor as PyLessDumbFeatureExtractor
from icecube import util

tray = I3Tray()

load("libdataio")
        
tray.AddModule("I3Reader", "reader",
               FileName= util.icdata_2007
               )

tray.AddModule(PyLessDumbFeatureExtractor, "pylessdumbfe",
               Launches_in = "InIceRawData",
               Hits_out = "pyhits",
               Pulses_out = "pypulses")


tray.AddModule(PyLineFit,"linefit",               
               InputRecoHits="pypulses",
               Name="LineFit2",
               )

tray.AddModule("TrashCan","adios")

tray.Execute()

tray.Finish()
