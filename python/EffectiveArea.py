#!/usr/bin/env python

#this script automatically generates massive amounts of histograms

import sys
from I3Tray import *
from loot import *
from glob import glob
from . import histos.WeightedHistogram
from math import *
import pylab

Ebins=8*5
sourcefiles=sys.argv[1:]
sourcefiles.sort()

i3file = dataio.I3File(sourcefiles[0])
frame = i3file.pop_physics()
weight=frame.Get("I3MCWeightDict")
SolidAngle=2*pi*(cos(weight["MinZenith"])-cos(weight["MaxZenith"]))
NEvents=weight["NEvents"]*len(sourcefiles)
MinEnergyLog=weight["MinEnergyLog"]
MaxEnergyLog=weight["MaxEnergyLog"]
DeltaLogE=(MaxEnergyLog-MinEnergyLog)/Ebins
i3file.close()

histogram=histos.WeightedHistogram.WeightedHistogram(MinEnergyLog, MaxEnergyLog, Ebins)

for file in sourcefiles:
    print("reading", file)
    i3file = dataio.I3File(file)
    while i3file.more():
        frame = i3file.pop_physics()
        weight=frame.Get("I3MCWeightDict")
        histogram.fill(log10(weight["PrimaryNeutrinoEnergy"]),weight["OneWeight"]/weight["PrimaryNeutrinoEnergy"]/NEvents/SolidAngle/DeltaLogE*1e-4)
                  
pylab.clf()
pylab.ylabel("Aeff [m^2]")
pylab.xlabel("log10(E/Gev)")
print(histogram.getXs(),histogram.getYs())
pylab.semilogy(histogram.getXs()+[9],histogram.getYs()+[0],linestyle='steps')
pylab.show()
