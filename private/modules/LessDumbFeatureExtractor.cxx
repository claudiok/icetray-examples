#include <examples/modules/LessDumbFeatureExtractor.h>

#include <dataclasses/OMKey.h>
#include <dataclasses/I3Map.h>
#include <dataclasses/physics/I3DOMLaunch.h>
#include <icetray/I3Frame.h>
#include <dataclasses/physics/I3RecoHit.h>
#include <dataclasses/physics/I3RecoPulse.h>

I3_MODULE(LessDumbFeatureExtractor);

LessDumbFeatureExtractor::LessDumbFeatureExtractor(const I3Context& context) :
  I3Module(context),
  launches_("InIceRawData")
{
  AddParameter("Launches",
	       "Name of the I3DOMLaunchSeriesMap in the frame to feature extract.",
	       launches_);

  AddOutBox("OutBox");
}

void LessDumbFeatureExtractor::Configure()
{
  GetParameter("Launches",launches_);
}

void LessDumbFeatureExtractor::Physics(I3FramePtr frame)
{
  const I3DOMLaunchSeriesMapConstPtr inIceResponse = 
    frame->Get<I3DOMLaunchSeriesMapConstPtr>(launches_);

  I3RecoHitSeriesMapPtr orhsm(new I3RecoHitSeriesMap());
  I3RecoPulseSeriesMapPtr orpsm(new I3RecoPulseSeriesMap());

  if(inIceResponse)
    {
      for(I3DOMLaunchSeriesMap::const_iterator iter = inIceResponse->begin() ;
	  iter != inIceResponse->end() ; 
	  iter++)
	{
	  assert(iter->second.size() > 0);
	  const I3DOMLaunch& launch = iter->second[0];

	  const std::vector<int>& waveform = launch.GetRawATWD(0);

	  assert(waveform.size() > 20);
	  int maxBin = 0;
	  int maxValue = waveform[0];
	  for(unsigned i = 0 ; i < 20 ; i++)
	    {
	      if(waveform[i] > maxValue)
		{
		  maxValue = waveform[i];
		  maxBin = i;
		}
	    }
	  log_trace("best bin: %d",maxBin);
	  double hitTime = ((double)maxBin )* 3.3;
	  hitTime += launch.GetStartTime();
	  log_trace("HitTime on OM (%d,%d): %f",
		    iter->first.GetString(),
		    iter->first.GetOM(),
		    hitTime);
      
	  I3RecoHit hit;
	  hit.SetTime(hitTime);
	  I3Vector<I3RecoHit> rhv;
	  rhv.push_back(hit);
	  (*orhsm)[iter->first] = rhv;

	  I3RecoPulse pulse;
	  pulse.SetTime(hitTime);
	  pulse.SetCharge(maxValue);
	  I3Vector<I3RecoPulse> rpv;
	  rpv.push_back(pulse);
	  (*orpsm)[iter->first] = rpv;
      
	}
    }

  frame->Put("hits",orhsm);
  frame->Put("pulses",orpsm);

  PushFrame(frame,"OutBox");
}

void LessDumbFeatureExtractor::Finish()
{
}
