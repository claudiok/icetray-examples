#include <examples/modules/AlmostSmartFeatureExtractor.h>

#include <dataclasses/OMKey.h>
#include <dataclasses/I3Map.h>
#include <dataclasses/physics/I3Waveform.h>
#include <icetray/I3Frame.h>
#include <dataclasses/physics/I3RecoHit.h>

I3_MODULE(AlmostSmartFeatureExtractor);

typedef I3Map<OMKey,I3Vector<I3Waveform> > Response;

AlmostSmartFeatureExtractor::
AlmostSmartFeatureExtractor(const I3Context& context) : I3Module(context)
{
  AddOutBox("OutBox");
}

void AlmostSmartFeatureExtractor::Configure()
{
}

void AlmostSmartFeatureExtractor::Physics(I3FramePtr frame)
{
  const Response& inIceResponse = 
    frame->Get<Response>("CalibratedATWD");

  I3RecoHitSeriesMapPtr orhsm(new I3RecoHitSeriesMap());

  for(Response::const_iterator iter = inIceResponse.begin() ;
      iter != inIceResponse.end() ; 
      iter++)
    {
      assert(iter->second.size() > 0);
      const vector<double> & waveform = iter->second[0].GetWaveform();

      assert(waveform.size() > 20);
      int maxBin = 0;
      double maxValue = waveform[0];
      for(unsigned i = 0 ; i < 20 ; i++)
	{
	  if(waveform[i] > maxValue)
	    {
	      maxValue = waveform[i];
	      maxBin = i;
	    }
	}
      log_trace("best bin: %d",maxBin);
      double binWidth = iter->second[0].GetBinWidth();
      double hitTime = ((double)maxBin )* binWidth;
      hitTime += iter->second[0].GetStartTime();
      log_trace("HitTime on OM (%d,%d): %f",
		iter->first.GetString(),
		iter->first.GetOM(),
		hitTime);
      
      I3RecoHit hit;
      hit.SetTime(hitTime);
      I3Vector<I3RecoHit> rhv;
      rhv.push_back(hit);
      (*orhsm)[iter->first] = rhv;
      
    }

  frame->Put("hits",orhsm);

  PushFrame(frame,"OutBox");
}

void AlmostSmartFeatureExtractor::Finish()
{
}
