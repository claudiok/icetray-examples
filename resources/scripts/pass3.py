#!/usr/bin/env python
#
# Pass 3:
#
# At this point, pass1.i3 contains, mostly frames that look like this:
#
# [ I3Frame :
#   'CalibratedData' ==> I3Map<OMKey, I3Vector<I3Waveform> >
#   'DrivingTime' ==> I3Time
#   'EventHeader' ==> I3EventHeader
#   'I3Calibration' ==> I3Calibration
#   'I3DetectorStatus' ==> I3DetectorStatus
#   'I3Geometry' ==> I3Geometry
#   'IceTopRawData' ==> I3Map<OMKey, I3Vector<I3DOMLaunch> >
#   'IceTopRecoHitSeries' ==> I3Map<OMKey, I3Vector<I3RecoHit> >
#   'InIceRawData' ==> I3Map<OMKey, I3Vector<I3DOMLaunch> >
#   'InIceRecoHitSeries' ==> I3Map<OMKey, I3Vector<I3RecoHit> >
#   'simpleseed' ==> I3Particle
# ]
#
# Now we'll make our first pass through the data going from one .i3
# file to another .i3 file.  This is easy.  We'll use the 'simpleseed'
# as the seed for a reconstruction which will later seed a different
# reconstruction.  The reader and writer services should look very
# familiar.
#
# After this you should take a look at the pass3.i3 file with the
# dataio-shovel.  Try highlighting the track that the reconstruction
# produced and hitting 'r' to get a root tree.
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
# the muxer gets events from the services above...
#
tray.AddModule("I3Reader","reader")(
    ("Filename", "pass1.i3")
    )

#
# You can imagine what this one does. it does.
#

tray.AddModule("SimpleReconstruction","simplereco")(
    ("InputHits","InIceRecoHitSeries"),
    ("OutputResult","pass1"),
    )

#
# the dump shows you what's going by as it happens
#
tray.AddModule("Dump","dump")


# Write the data with our new reconstruction.  Same usage of the
# writer as in pass1.
tray.AddModule("I3Writer","writer")(
    ("filename", "pass3.i3")
    )

#
# The usual trashcan-at-the-end idiom.
#
tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()
