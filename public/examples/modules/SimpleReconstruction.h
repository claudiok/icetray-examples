#ifndef SIMPLERECONSTRUCTION_H
#define SIMPLERECONSTRUCTION_H

#include <icetray/I3Module.h>

/**
 * @brief A simple reconstruction. Not physical.  Just simple.
 */
class SimpleReconstruction : public I3Module
{
 public:
  /**
   * @brief Constructor requires an I3Context be passed in
   */
  SimpleReconstruction(const I3Context& context);

  /**
   * @brief This module is configurable, so we write the configure method
   */
  void Configure();

  /**
   * @brief This method does the work of reconstructing the data that
   * is located in the frame that gets passed in.
   */
  void Physics(I3FramePtr frame);

 private:
  
  // these variables will hold the parameters that we take from the user
  std::string inputHits_;
  std::string outputResult_;
};

#endif
