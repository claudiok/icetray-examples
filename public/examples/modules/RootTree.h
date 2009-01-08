#ifndef EXAMPLES_DELTAANGLE_H_INCLUDED
#define EXAMPLES_DELTAANGLE_H_INCLUDED

#include <icetray/I3Module.h>
#include <string>
#include <vector>

//
// Example module: calculate delta-angle
//
class RootTree : public I3Module
{
  // The names of the thing to treeize and its class name.
  std::string key_, classname_, filename_;

 public:

  RootTree(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

  void Finish();

};

#endif
