#ifndef EXAMPLES_NAMEDFIBONACCISERVICEFACTORY_H_INCLUDED
#define EXAMPLES_NAMEDFIBONACCISERVICEFACTORY_H_INCLUDED

#include <icetray/I3ServiceFactory.h>
#include <examples/services/FibonacciService.h>

// 
//  
//
class NamedFibonacciServiceFactory 
  : public I3ServiceFactory
{
  std::string name_;
 public:

  virtual ~NamedFibonacciServiceFactory() { }

  NamedFibonacciServiceFactory(const I3Context& context) 
    : I3ServiceFactory(context)

    { 
      // default name for the service is, in this case, its I3DefaultName
      name_ = I3DefaultName<SequenceService>::value();

      AddParameter("name",
		   "Where to install the service. Default is at DefaultName",
		   name_);
    }

  void Configure()
  {
    GetParameter("name", name_);
    log_trace("will install at %s", name_.c_str());
  }

  bool InstallService(I3Context& context) 
  {
    // for every context we create a new service and add it
    SequenceServicePtr singleton_service(new FibonacciService);

    // this will install under the SequenceService's DefaultName
    context.Put(name_, singleton_service);
    return true;
  }
};

#endif
