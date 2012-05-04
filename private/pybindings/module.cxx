#include <examples/services/FibonacciService.h>
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
}

