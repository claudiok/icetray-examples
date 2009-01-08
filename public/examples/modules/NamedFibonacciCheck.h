#ifndef EXAMPLES_NAMEDFIBONACCICHECK_H_INCLUDED
#define EXAMPLES_NAMEDFIBONACCICHECK_H_INCLUDED

#include <icetray/I3Module.h>
#include <string>

class I3Context;

class NamedFibonacciCheck : public I3Module
{
  unsigned prev_, prev_prev_;
  std::string where_;

 public:

  NamedFibonacciCheck(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

};

#endif
