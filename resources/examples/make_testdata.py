#!/usr/bin/env python

from I3Tray import *
from os.path import *
import sys

load("libdataclasses")
load("libdataio")
load("libphys-services")
load("libdaq-decode")
load("libpayload-parsing")
load("libI3Db")
load("libDOMcalibrator")
load("libicepick")

workspace = expandvars("$I3_SRC")

dbserver = "dbs2.icecube.wisc.edu"

if len(sys.argv) != 2:
    print "Must run with an arguement specifying the full path of the PFRaw file."
    sys.exit(1)
infile = sys.argv[1]

tray = I3Tray()

## Some OMKey/channel translation services

tray.AddService("I3XMLOMKey2MBIDFactory","omkey2mbid",
                infile=workspace + "/phys-services/resources/mainboard_ids.xml.gz")

tray.AddModule("I3Reader","reader",
               fileName = infile,
               )

tray.AddService("I3DbGeometryServiceFactory","geometry",
                host = dbserver,
                )

tray.AddService("I3DbCalibrationServiceFactory","calibration",
                host = dbserver,
                )

tray.AddService("I3DbDetectorStatusServiceFactory","status",
                host = dbserver
                )

tray.AddService("I3PayloadParsingEventDecoderFactory","i3eventdecode",
                )


tray.AddModule("QConverter", "qify")
tray.AddModule("I3MetaSynth","muxme")

#tray.AddModule("Dump","dump")

def data_check(frame):
    if frame.Has("I3DAQData"):
        return True
    else:
        return False

tray.AddModule(data_check,"daqthere",Streams=[icetray.I3Frame.DAQ])

tray.AddModule("I3FrameBufferDecode","i3decode",
               BufferID = "I3DAQData"
               )

tray.AddModule("Remix", "remix");

#tray.AddModule("I3DOMcalibrator","calibrate-inice",
#               InputRawDataName = "InIceRawData"
#               )


hitThreshold = 10
tray.AddModule("I3IcePickModule<I3PickRawNHitEventFilter>","filter",
               DiscardEvents = True,
               HitThresholdLow = hitThreshold
               )


skippers = ["I3DAQData",
            "moonfit"]

tray.AddModule("I3Writer","writer",
               SkipKeys = skippers,
               filename = "TEST_DATA.i3",
                DropOrphanStreams=[icetray.I3Frame.DAQ]
               )

#tray.AddModule("Dump","dump2")

tray.AddModule("TrashCan","trash")

tray.Execute(20)
tray.Finish()
