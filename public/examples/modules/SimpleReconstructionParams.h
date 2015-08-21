#ifndef SIMPLERECONSTRUCTIONPARAMS_H
#define SIMPLERECONSTRUCTIONPARAMS_H

#include <icetray/I3FrameObject.h>

// must inherit from I3FrameObject if it's going to go in the frame
class SimpleReconstructionParams : public I3FrameObject
{
 public:
  // the data
  double simplicity;
  double austerity;
  double candor;
  double clarity;

  // serialization routine
  template <class Archive>
    void serialize(Archive& ar, unsigned version);
  
  SimpleReconstructionParams() : 
    simplicity(NAN),
    austerity(NAN),
    candor(NAN),
    clarity(NAN)
    {}
  
  // needs a virtual destructor implemented in the .cxx file
  virtual ~SimpleReconstructionParams();

};

// optional but gives some boost::shared_ptr typedefs
I3_POINTER_TYPEDEFS(SimpleReconstructionParams);

#endif
