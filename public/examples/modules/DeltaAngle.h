#ifndef EXAMPLES_DELTAANGLE_H_INCLUDED
#define EXAMPLES_DELTAANGLE_H_INCLUDED

#include <icetray/I3Module.h>
#include <string>
#include <vector>

//
// Example module: calculate delta-angle
//
class DeltaAngle : public I3Module
{
  // names of two particles to compare.  Generally, a module needs to
  // be told where to look for things in the frame and where to put
  // its results.  This keeps it "modular", as a module should be.  It
  // is reusable without recompiling.
  std::string key_lhs_, key_rhs_, th1_fname_;

  // For the sake of keeping the code clear, we'll accumulate the
  // angles in a vector and calculate things in our Finish() method, .
  std::vector<double> angles_;

 public:

  DeltaAngle(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

  void Finish();

};

#endif
