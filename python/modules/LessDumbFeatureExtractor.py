from icecube import icetray, dataclasses, phys_services

class LessDumbFeatureExtractor(icetray.I3Module):
    def __init__(self, context):
        icetray.I3Module.__init__(self, context)
        self.AddParameter("Launches_in",
                          "Where to get the launches",
                          None)
        self.AddParameter("Hits_out",
                          "Where to put FE Hits",
                          "fehits")
        self.AddParameter("Pulses_out",
                          "Where to put FE Hits",
                          "fepulses")
        self.AddOutBox("OutBox")

    def Configure(self):
        self.launchesname = self.GetParameter("Launches_in")
        self.ohitsname = self.GetParameter("Hits_out")
        self.opulsesname = self.GetParameter("Pulses_out")
    
    def DAQ(self, frame):
        launches = frame.Get(self.launchesname)

        if not launches:
            self.PushFrame(frame)
            return
        
        print("yah launches")

        ohits = dataclasses.I3RecoHitSeriesMap()
        opulses = dataclasses.I3RecoPulseSeriesMap()

        for entry in launches:
            om = entry.key()
            launch = entry.data()[0]
            waveform = launch.GetRawATWD(0)
            print(waveform)

            maxbin = 0
            maxvalue = waveform[0];
            for i in range(1,20):
                if maxvalue < waveform[i]:
                    maxvalue = waveform[i]
                    maxbin = i
                    
            print(maxbin, maxvalue)

            hit = dataclasses.I3RecoHit()
            hittime = launch.GetStartTime() + maxbin * 3.3

            hit.Time = hittime
            vrh = dataclasses.vector_I3RecoHit()
            vrh.append(hit)
            ohits[om] = vrh
            
            pulse = dataclasses.I3RecoPulse()
            pulse.Time = hittime
            pulse.Charge = maxvalue
            vrp = dataclasses.vector_I3RecoPulse()
            vrp.append(pulse)
            opulses[om] = vrp


        frame.Put(self.ohitsname, ohits)
        frame.Put(self.opulsesname, opulses)
        self.PushFrame(frame)

        
