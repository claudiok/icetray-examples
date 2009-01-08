#include <examples/modules/PutParticle.h>

#include <icetray/I3Frame.h>
#include <icetray/I3Units.h>
#include <dataclasses/physics/I3Particle.h>

using namespace std;

I3_MODULE(PutParticle);

PutParticle::PutParticle(const I3Context& context) : 
  I3Module(context)
{
  // tell the framework that we have an outbox...
  AddOutBox("OutBox");

  where_ = "UNSET";
  AddParameter("Where", "Where to put it", where_);

  zenith_ = 0.0;
  AddParameter("Zenith", "Zenith value of new particle", zenith_);

  azimuth_ = 0.0;
  AddParameter("Azimuth", "Azimuth value of new particle", azimuth_);

}

void 
PutParticle::Configure()
{
  // this fetches the configured values from the steering file and
  // puts them into the local variables.
  GetParameter("Where", where_);
  GetParameter("Zenith", zenith_);
  GetParameter("Azimuth", azimuth_);
}

//
//  Create particles and put them in the frames...
//
void 
PutParticle::Physics(I3FramePtr frame)
{
  I3ParticlePtr particle(new I3Particle(I3Particle::InfiniteTrack,I3Particle::MuPlus));
  particle->SetDir(zenith_, azimuth_);

  frame->Put(where_, particle);

  PushFrame(frame);

}

