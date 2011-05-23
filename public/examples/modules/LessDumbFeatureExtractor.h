#ifndef LESSDUMBFEATUREEXTRACTOR_H
#define LESSDUMBFEATUREEXTRACTOR_H

#include <icetray/I3Module.h>

class LessDumbFeatureExtractor : public I3Module
{
 public:
  LessDumbFeatureExtractor(const I3Context& context);

  void DAQ(I3FramePtr frame);

  void Configure();

  void Finish();

 private:
  std::string launches_;
};

#endif
