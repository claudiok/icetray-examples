#include <examples/services/FibonacciService.h>
#include <examples/MutineerTrack.h>
#include <icetray/python/context_suite.hpp>
#include <iostream>

#include <icetray/load_project.h>

using namespace boost::python;

void blam()
{
  std::cout << "blam\n";
}

BOOST_PYTHON_MODULE(examples)
{

  load_project("examples", false); 

  def("blam", blam);

  // Pull a SequenceService out of the I3Context
  class_<SequenceService, boost::shared_ptr<SequenceService>, boost::noncopyable>("SequenceService", boost::python::no_init)
    .def(icetray::python::context_suite<SequenceService>())
    .def("next", &SequenceService::next)
  ;

  class_<MutineerTrack, boost::shared_ptr<MutineerTrack>, bases<I3Particle> >("MutineerTrack")
    .def_readwrite("ye", &MutineerTrack::ye)
    .def_readwrite("scurvy", &MutineerTrack::scurvy)
    .def_readwrite("dogs", &MutineerTrack::dogs)
    ;
}

