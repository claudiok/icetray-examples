#include "examples/modules/SimpleReconstruction.h"
#include "examples/modules/SimpleReconstructionParams.h"
#include <dataclasses/physics/I3Particle.h>
#include <dataclasses/geometry/I3Geometry.h>
#include <dataclasses/physics/I3RecoHit.h>
#include <icetray/I3Frame.h>

// This macro is used to export the module name to the framework
I3_MODULE(SimpleReconstruction);

SimpleReconstruction::SimpleReconstruction(const I3Context& context) : 
  I3Module(context),
  inputHits_("hits"),
  outputResult_("simpleReco")
{
  // specify that this module has one outbox named 'OutBox'
  AddOutBox("OutBox");

  // this is how we specify that we want to take these two parameters
  AddParameter("InputHits",
	       "Name of the hit series map that we will take in",
	       inputHits_);

  AddParameter("OutputResult",
	       "Name of the final reconstruction result in the frame",
	       outputResult_);
	 
}

void SimpleReconstruction::Configure()
{
  // getting the parameters from the userx
  GetParameter("InputHits",
	       inputHits_);

  GetParameter("OutputResult",
	       outputResult_);

  // at this point in the code we should have the final configured values
  // so we can log_trace the values we wil use
  log_trace("Will reconstruct based on the %s hit series",
	    inputHits_.c_str());
  log_trace("Will output a reconstruction result named %s",
	    outputResult_.c_str());


}

void SimpleReconstruction::Physics(I3FramePtr frame)
{
  // finding the hits.
  const I3RecoHitSeriesMap& hits = frame->Get<I3RecoHitSeriesMap>(inputHits_);

  // finding the geometry.  The geometry is special 'cause you
  // don't need a key for it.
  const I3Geometry& geometry = frame->Get<I3Geometry>();


  // computing average position of all the hits
  double avg_x = 0;
  double avg_y = 0;
  double avg_z = 0;
  double avg_t = 0;
  double nHit = 0.0;
  for(I3RecoHitSeriesMap::const_iterator iter = hits.begin() ; 
      iter != hits.end() ; 
      iter++)
    {
      I3OMGeoMap::const_iterator foundGeometry = 
	geometry.omgeo.find(iter->first);
      if(foundGeometry == geometry.omgeo.end())
	{
	  log_fatal("OMKey (%d,%d) is not located in the geometry",
		    iter->first.GetString(),
		    iter->first.GetOM());
	}

      const I3RecoHitSeries& rhs= iter->second;
      for(I3RecoHitSeries::const_iterator hitIter = rhs.begin() ; 
	  hitIter != rhs.end() ; 
	  hitIter++)
	{
	  avg_x += foundGeometry->second.position.GetX();
	  avg_y += foundGeometry->second.position.GetY();
	  avg_z += foundGeometry->second.position.GetX();
	  avg_t += hitIter->GetTime();
	  nHit +=1.0;
	} 
	  
    }
  avg_x /= nHit;
  avg_y /= nHit;
  avg_z /= nHit;
  avg_t /= nHit;

  // filling the particle for the frame
  I3ParticlePtr particle(new I3Particle());
  particle->SetShape(I3Particle::InfiniteTrack);
  particle->SetPos(avg_x,avg_y,avg_z);
  particle->SetTime(avg_t);
  particle->SetDir(0,0);

  // if it's garbage, identify it as such
  if(finite(avg_x * avg_y * avg_z * avg_t))
    particle->SetFitStatus(I3Particle::OK);
  else
    particle->SetFitStatus(I3Particle::InsufficientHits);

  // the 'reconstruction-specific' stuff that isn't in dataclasses
  SimpleReconstructionParamsPtr result(new SimpleReconstructionParams());
  result->simplicity = exp(avg_x * avg_y);
  result->candor = avg_y * avg_x * avg_z;
  result->austerity = 1.0;
  result->clarity = 1./avg_t;

  // putting it in the frame
  frame->Put(outputResult_,particle);
  frame->Put(string(outputResult_ + "Params"),result);
  
  // giving the frame back to the framework
  PushFrame(frame,"OutBox");

}
