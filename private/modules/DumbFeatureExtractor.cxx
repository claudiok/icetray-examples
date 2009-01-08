#include <examples/modules/DumbFeatureExtractor.h>
#include <icetray/I3Frame.h>
#include <icetray/OMKey.h>
#include <dataclasses/physics/I3DOMLaunch.h>
#include <dataclasses/physics/I3RecoHit.h>
#include <dataclasses/I3Map.h>
#include <dataclasses/physics/I3DOMLaunch.h>
#include <icetray/I3Context.h>
#include <icetray/I3Configuration.h>
#include <vector>
#include <map>

I3_MODULE(DumbFeatureExtractor);

DumbFeatureExtractor::DumbFeatureExtractor(const I3Context& context) : 
  I3Module(context), 
  inputResponse_("InIceRawData"),
  outputSeries_("InIceRecoHitSeries"),
  featureExtractIceTop_(1)
{
  AddOutBox("OutBox");

  AddParameter("InputResponse","",inputResponse_);
  AddParameter("OutputSeries","",outputSeries_);
  AddParameter("FeatureExtractIceTop","",featureExtractIceTop_);
}

void DumbFeatureExtractor::Configure()
{
  GetParameter("InputResponse",inputResponse_);
  GetParameter("OutputSeries",outputSeries_);
  GetParameter("FeatureExtractIceTop",featureExtractIceTop_);
}

void DumbFeatureExtractor::Physics(I3FramePtr frame)
{
  // in ice
  {
    const I3Map<OMKey,I3DOMLaunchSeries>& inIceResponses 
      = frame->Get<I3Map<OMKey,I3DOMLaunchSeries> >(inputResponse_);
    shared_ptr<I3Map<OMKey,I3RecoHitSeries> > 
      inIceSeries(new I3Map<OMKey,I3RecoHitSeries> );
    for(I3Map<OMKey,I3DOMLaunchSeries>::const_iterator iter = inIceResponses.begin() ; 
	iter != inIceResponses.end() ; 
	iter++)
      {
	if(iter->second.size() > 0)
	(*inIceSeries)[iter->first] = I3RecoHitSeries();
	FillSeries((*inIceSeries)[iter->first],iter->second[0]);
      }
    frame->Put(outputSeries_, inIceSeries);
  }
  
  // ice top
  if(featureExtractIceTop_)
  {
    const I3Map<OMKey,I3DOMLaunchSeries>& iceTopResponses 
      = frame->Get<I3Map<OMKey,I3DOMLaunchSeries> >("IceTopRawData");
    shared_ptr<I3Map<OMKey,I3RecoHitSeries> > 
      iceTopSeries(new I3Map<OMKey,I3RecoHitSeries> );
    for(I3Map<OMKey,I3DOMLaunchSeries>::const_iterator iter = iceTopResponses.begin() ; 
	iter != iceTopResponses.end() ; 
	iter++)
      {
	if(iter->second.size() > 0)
	  {
	    (*iceTopSeries)[iter->first] = I3RecoHitSeries();
	    FillSeries((*iceTopSeries)[iter->first],iter->second[0]);
	  }
      }
    frame->Put("IceTopRecoHitSeries", iceTopSeries);
  }
  
  PushFrame(frame,"OutBox");

}


void DumbFeatureExtractor::FillSeries(I3RecoHitSeries& series,
					const I3DOMLaunch& launch)
{
  I3RecoHit hit;
  hit.SetTime(launch.GetStartTime());
  series.push_back(hit);
}
