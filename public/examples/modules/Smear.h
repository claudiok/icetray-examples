#ifndef EXAMPLES_SMEAR_H_INCLUDED
#define EXAMPLES_SMEAR_H_INCLUDED

#include <icetray/I3Module.h>
#include <icetray/OMKey.h>
#include <string>
#include <vector>

#include <phys-services/I3RandomService.h>
#include <examples/Gaussian.h>

//
//  Another little example: add noise to tracks that go by.  This
//  module is half toy, half useful when verifying that
//  testing/graphing modules work.
//
class Smear : public I3Module
{
  // where to take the seed, where to put the output
  std::string seed_key_, output_key_;

  double mu_;
  double sigma_;
  double constant_;

  I3RandomService &rnd;

  // and thats a gaussian.  We can't use the I3RandomService's Gaus()
  // as we're acutally smearing by the "Turcan Distribution" sin(x) *
  // gaus(x), x in [0,Pi)
  Gaussian gaussian;
  
 public:

  Smear(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

  SET_LOGGER("Smear");
};

#endif
