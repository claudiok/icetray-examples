#ifndef EXAMPLES_HELLOCONFIGURATION_H_INCLUDED
#define EXAMPLES_HELLOCONFIGURATION_H_INCLUDED

#include <icetray/I3Module.h>
#include <icetray/OMKey.h>
#include <string>
#include <vector>

class HelloConfiguration : public I3Module
{
  int an_int_;
  bool a_bool_;
  OMKey an_omkey_;
  double a_double_;

  std::string a_string_;
  std::vector<int> vector_of_ints_;
  std::vector<unsigned long> vector_of_ulongs_;
  std::vector<double> vector_of_doubles_;
  std::vector<OMKey> vector_of_omkeys_;
  std::vector<std::string> vector_of_strings_;

 public:

  HelloConfiguration(const I3Context& context);

  void Configure();
  
  void Physics(I3FramePtr frame);

};

#endif
