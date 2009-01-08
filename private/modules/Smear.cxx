#include <icetray/I3Frame.h>
#include <icetray/I3Units.h>
#include <icetray/I3Context.h>

#include <phys-services/I3Calculator.h>
#include <dataclasses/physics/I3Particle.h>
#include <examples/modules/Smear.h>
#include <examples/Gaussian.h>

#include <cmath>

using namespace std;

I3_MODULE(Smear);
 
Smear::Smear (const I3Context& context) : 
  I3Module(context), 
  rnd(context_.Get<I3RandomService>()) // notice we keep a reference
				       // to whatever RandomService
				       // the tray has decided to
				       // provide us through our I3Context
{
  // tell the framework that we have an outbox...
  AddOutBox("OutBox");

  // inform the framework of our parameters and their default values
  seed_key_ = "UNSET";
  AddParameter("Src", "Source particle", seed_key_);

  output_key_ = "UNSET";
  AddParameter("Dst", "Destination for smeared particle", output_key_);

  mu_ = 0.0;
  AddParameter("Mean", "Mean of smearing (normal) distribution", mu_);

  constant_ = 0.0;
  AddParameter("Constant", "Add constant value to smear", constant_);

  sigma_ = 0.0;
  AddParameter("Sigma", "Sigma of smearing (normal) distribution", sigma_);

}

void 
Smear::Configure()
{
  // this fetches the configured values from the steering file and
  // puts them into the local variables.
  GetParameter("Src", seed_key_);
  GetParameter("Dst", output_key_);
  GetParameter("Mean", mu_);
  GetParameter("Sigma", sigma_);
  GetParameter("Constant", constant_);

  log_trace("Creating normal distribution mean=%f deg sigma=%f", 
	    mu_, sigma_);

  gaussian = Gaussian(mu_, sigma_);
}

void 
Smear::Physics(I3FramePtr frame)
{
  // One always prefers const references to const pointers, but in
  // this case particles might be missing, so we get the particle as a
  // pointer and then check the pointer for nullness.
  I3ParticleConstPtr seed = frame->Get<I3ParticleConstPtr>(seed_key_);

  // If there aren't any particles called "seed_key_" skip it.
  if (!seed)
    {
      PushFrame(frame);  // it's not just "return", it's PushFrame, then return.
      return;
    }

  // copy construct a new particle from the shared pointer to the seed.
  I3ParticlePtr smeared_particle;
  if (seed)
    smeared_particle = I3ParticlePtr(new I3Particle(*seed));

  // smear Zenith by numbers with the distribution (sin(x) * gaus(x)) on [0,Pi)
  // which has maximum value ~ 0.28 on that interval.

  const double max_y = 0.25; // just a little higher than actual max.
  double smear = 0.0;

  // if we're actually using random numbers, do it now, otherwise skip
  if (sigma_ > 0)
    while (true)
      {
	smear = rnd.Uniform(0, M_PI);
	double reject_prob = std::sin(smear) * gaussian(smear);
	double reject = rnd.Uniform(0, max_y);

	if (reject > reject_prob)
	  continue; // skip it, try another.

	break;
      }

  // smear track and return
  smeared_particle->SetDir(seed->GetZenith() + smear + constant_, 
			   seed->GetAzimuth());

  frame->Put(output_key_, smeared_particle);
  PushFrame(frame);
}

