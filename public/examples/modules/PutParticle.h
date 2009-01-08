#ifndef EXAMPLES_PUTPARTICLE_H_INCLUDED
#define EXAMPLES_PUTPARTICLE_H_INCLUDED

#include <icetray/I3Module.h>
#include <string>

//
//  Create particles with the given zen/azi and put them in the frame
//  under the specified name.  You can use them as seed tracks, smear
//  them and check your graphing software, use them to fill frames to
//  benchmark data i/o, you name it.
//
class PutParticle : public I3Module
{
  // where to put them
  std::string where_;

  // their direction
  double zenith_, azimuth_;

 public:

  PutParticle (const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

};

#endif
