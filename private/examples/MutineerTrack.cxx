#include <icetray/serialization.h>
#include <examples/MutineerTrack.h>

#include <iostream>
using std::cout;

template <typename Archive>
void 
MutineerTrack::serialize(Archive & ar, unsigned)
{
  ar & make_nvp("I3Particle", base_object<I3Particle>(*this));
  ar & make_nvp("ye", ye);
  ar & make_nvp("scurvy", scurvy);
  ar & make_nvp("dogs", dogs);
}

I3_SERIALIZABLE(MutineerTrack);



