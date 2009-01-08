#ifndef EXAMPLES_DUMBFEATUREEXTRACTOR_H
#define EXAMPLES_DUMBFEATUREEXTRACTOR_H

#include <icetray/I3Module.h>
#include <dataclasses/physics/I3RecoHit.h>

class I3DOMLaunch;

class DumbFeatureExtractor : public I3Module
{
 public:
  DumbFeatureExtractor(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

  void FillSeries(I3RecoHitSeries&, const I3DOMLaunch&);

 private:
  string inputResponse_;
  string outputSeries_;
  bool featureExtractIceTop_; // if true run on IceTop, otherwise skip it
};

#endif
