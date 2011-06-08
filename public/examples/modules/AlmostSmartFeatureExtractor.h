#ifndef ALMOSTSMARTFEATUREEXTRACTOR_H
#define ALMOSTSMARTFEATUREEXTRACTOR_H

#include <icetray/I3Module.h>

class AlmostSmartFeatureExtractor : public I3Module
{
 public:
  AlmostSmartFeatureExtractor(const I3Context& context);

  void DAQ(I3FramePtr frame);

  void Configure();

  void Finish();
};

#endif
