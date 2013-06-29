#!/usr/bin/env python

# Can we get an instance of an abstract I3Service base class from
# the context?

from icecube import icetray, examples, dataio

import I3Tray

tray = I3Tray.I3Tray()

tray.AddService("NamedFibonacciServiceFactory", "fibi", name="fibi")

class FibCheck(icetray.I3Module):
	def __init__(self, ctx):
		icetray.I3Module.__init__(self, ctx)
		self.AddOutBox("OutBox")
	def Configure(self):
		pass
	def DAQ(self, frame):
		self.fibs = examples.SequenceService.from_context(self.context, "fibi")
		nums = [next(self.fibs) for i in range(10)]
		print('I got some numbers for ya: %s' % (nums, ))
		self.PushFrame(frame)
		
tray.AddModule("I3InfiniteSource", "gaping_maw")

tray.AddModule(FibCheck, "check")

tray.AddModule("TrashCan", "YesWeCan")
tray.Execute(1)

tray.Finish()
