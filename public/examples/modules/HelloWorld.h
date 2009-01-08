#ifndef EXAMPLES_HELLOWORLD_H
#define EXAMPLES_HELLOWORLD_H

#include <icetray/I3Module.h>
#include <string>

class HelloWorld : public I3Module
{
  std::string where_;
  std::string say_what_;

 public:

  HelloWorld(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

};

#endif
