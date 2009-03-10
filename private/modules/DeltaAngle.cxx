#include <examples/modules/DeltaAngle.h>

#include <icetray/I3Frame.h>
#include <icetray/I3Context.h>
#include <icetray/I3Units.h>
#include <phys-services/I3Calculator.h>
#include <dataclasses/physics/I3Particle.h>

#ifdef I3_USE_ROOT
  #include <TFile.h>
  #include <TH1D.h>
#endif

using namespace std;

I3_MODULE(DeltaAngle);


DeltaAngle::DeltaAngle(const I3Context& context) : 
  I3Module(context)
{
  // tell the framework that we have an outbox...
  AddOutBox("OutBox");

  // inform the framework of our parameters and their default values
  key_lhs_ = "UNSET";
  AddParameter("lhs", "Left hand side name", key_lhs_);

  key_rhs_ = "UNSET";
  AddParameter("rhs", "Right hand side name", key_rhs_);

  #ifdef I3_USE_ROOT
	th1_fname_ = "DeltaAngle";
	AddParameter("th1_fname", "Filename for TH1", th1_fname_);
  #endif
}

void DeltaAngle::Configure()
{
  // this fetches the configured values from the steering file and
  // puts them into the local variables.
  GetParameter("lhs", key_lhs_);
  GetParameter("rhs", key_rhs_);
  GetParameter("th1_fname", th1_fname_);
}

//
//  Here we just pull pairs of Particles out of the frame and store
//  the angle between them for later.
//
void 
DeltaAngle::Physics(I3FramePtr frame)
{
  // One always prefers const references to const pointers, but in
  // this case particles might be missing.
  I3ParticleConstPtr lhs = frame->Get<I3ParticleConstPtr>(key_lhs_);
  I3ParticleConstPtr rhs = frame->Get<I3ParticleConstPtr>(key_rhs_);

  // shared pointers evaluate in bool contexts just like regular
  // pointers.  We'll skip events where one or both of the particles
  // we've been told to examine are missing
  if (!lhs || !rhs)
    {
      // Important!  Don't forget to push your frame.
      PushFrame(frame);
      return;
    }

  // our friend Mr. Vector will expand as necessary to hold what it
  // needs
  double angle = I3Calculator::Angle(*lhs, *rhs);
  angles_.push_back(angle);
  
  PushFrame(frame);
}

//
//  Here we are given the opportunity to do what we like before the
//  tray shuts down.  We'll make some numbers with our vector, spit
//  out a histogram, that kind of thing.
//
void
DeltaAngle::Finish()
{
#ifdef I3_USE_ROOT
  TFile tfile(th1_fname_.c_str(), "UPDATE", "DeltaAngle module output", 0);

  string histotitle = key_lhs_ + " vs. " + key_rhs_;
  TH1D th1d(GetName().c_str(), histotitle.c_str(), 100, 0, 180);

  for (unsigned i=0; i<angles_.size(); i++)
    th1d.Fill(angles_[i]/I3Units::degree);

  th1d.Write();
  tfile.Close();
#endif
}
