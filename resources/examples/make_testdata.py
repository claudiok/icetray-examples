#!/usr/bin/env python

from I3Tray import *
from os.path import *
import sys

load("libdataclasses")
load("libdataio")
load("libphys-services")
load("libtwr-decode")
load("libdaq-decode")
load("libpayload-parsing")
load("libI3Db")
load("libamanda-core")
load("libDOMcalibrator")
load("libicepick")

workspace = expandvars("$I3_SRC")

dbserver = "dbs2.icecube.wisc.edu"

if len(sys.argv) != 2 and sys.argv[1].find("Raw") < 0 :
    print "Must run with an arguement specifying the full path of the PFRaw file."
    sys.exit(1)
infile = sys.argv[1]

tray = I3Tray()

## Some OMKey/channel translation services
tray.AddService("I3XMLOMKey2MBIDFactory","omkey2mbid")(
    ("infile",workspace + "/phys-services/resources/mainboard_ids.xml")
    )
tray.AddService("TWRXMLTWRKey2ChannelIDFactory","twrkey2channelid")(
    ("files",[workspace + "/twr-decode/resources/ChannelID_TWRKey.xml"])
    )
tray.AddService("I3XMLChannelID2OMKeyFactory","channelid2omkey")(
    ("infile",workspace + "/amanda-core/resources/channel_ids.xml")
    )

tray.AddService("I3ReaderServiceFactory","reader")(
    ("FileName",infile),
    ("OmitGeometry",True),
    ("OmitCalibration",True),
    ("OmitStatus",True),
    ("SkipMissingDrivingTime",True),
    ("SkipKeys",["I3DST","TWRDAQData*"])
    )

tray.AddService("I3DbGeometryServiceFactory","geometry")(
    ("host",dbserver)
    )

tray.AddService("I3DbCalibrationServiceFactory","calibration")(
    ("host",dbserver)
    )

tray.AddService("I3DbDetectorStatusServiceFactory","status")(
    ("host",dbserver)
    )

## Decoding services
#tray.AddService("TWRStandardDAQEventDecoderFactory","twreventdecode")(
#   ("headerid","TWRDAQEventHeader"),
#    )

tray.AddService("I3PayloadParsingEventDecoderFactory","i3eventdecode")(
    ("Year",2007),
    ("headerid",""),
    ("triggerid",""),
    ("specialdataid","SyncPulseMap"),
    ("specialdataoms",[OMKey(0,91),OMKey(0,92)])
    )

tray.AddModule("I3Muxer","muxme")

tray.AddModule("I3FrameBufferDecode","i3decode")(
   ("BufferID","I3DAQData")
   )

#tray.AddModule("TWRFrameBufferDecode","twrdecode")(
#   ("BufferID","TWRDAQData")
#   )

hitThreshold = 20

tray.AddModule("I3IcePickModule<I3PickRawNHitEventFilter>","filter")(
    ("DiscardEvents",True),
    ("HitThresholdLow", hitThreshold)
    )


tray.AddModule("I3DOMcalibrator","calibrate-inice")(
    ("InputRawDataName","InIceRawData")
    )

tray.AddModule("I3Writer","writer")(
    ("SkipKeys",["I3DAQData","TWRDAQData*","ToI","cascade-linefit","filterMask","iclinefit","moonfit"]),
    ("filename","2007_JEB_DATA.i3")
    )

tray.AddModule("Dump","dump")

tray.AddModule("TrashCan","trash")

tray.Execute(500)
tray.Finish()
