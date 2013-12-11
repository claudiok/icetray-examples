#ifndef MUTINEERTRACK_H_INCLUDED
#define MUTINEERTRACK_H_INCLUDED

#include <dataclasses/physics/I3Particle.h>

struct MutineerTrack : public I3Particle
{

  double ye, scurvy, dogs;

public:

  template <typename Archive>
  void serialize(Archive & ar, unsigned version);

};

#endif
