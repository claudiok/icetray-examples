#ifndef EXAMPLES_SEQUENCESERVICE_H
#define EXAMPLES_SEQUENCESERVICE_H

#include <icetray/I3DefaultName.h>
#include <icetray/I3PointerTypedefs.h>

// This is the base class for a family of 'SequenceService's that can
// be plugged in to an icetray.  Note that this class stands
// compeletly on its own: It needn't inherit from anything, it defines
// a pure virtual interface to some "service", in this case a service
// that returns some sequence of unsigned integers.

class SequenceService
{

 public:

  virtual ~SequenceService() { }

  SequenceService() { }

  virtual unsigned next() = 0;

};

I3_DEFAULT_NAME(SequenceService);
I3_POINTER_TYPEDEFS(SequenceService);

#endif
