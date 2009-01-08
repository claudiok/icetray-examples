#ifndef EXAMPLES_FIBONACCICHECK_H_INCLUDED
#define EXAMPLES_FIBONACCICHECK_H_INCLUDED

#include <icetray/I3Module.h>
#include <string>

class I3Context;

class FibonacciCheck : public I3Module
{
  unsigned prev_, prev_prev_;

 public:

  FibonacciCheck(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

};

#endif
