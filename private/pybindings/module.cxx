#include <icetray/load_project.h>
#include <iostream>

using namespace boost::python;

void blam()
{
  std::cout << "blam\n";
}

BOOST_PYTHON_MODULE(examples)
{
  load_project("libexamples", false);
  def("blam", blam);
}

