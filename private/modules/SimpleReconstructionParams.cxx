#include <icetray/serialization.h>
#include "examples/modules/SimpleReconstructionParams.h"

SimpleReconstructionParams::~SimpleReconstructionParams()
{
}


template <class Archive>
void SimpleReconstructionParams::serialize(Archive& ar,unsigned version)
{
  // must serialize the base object
  ar & make_nvp("I3FrameObject", base_object<I3FrameObject>(*this));

  // and all the data members
  ar & make_nvp("simplicity",simplicity);
  ar & make_nvp("austerity",austerity);
  ar & make_nvp("candor",candor);
  ar & make_nvp("clarity",clarity);
  
}

// this macro instantiates all the needed serialize methods
I3_SERIALIZABLE(SimpleReconstructionParams);
