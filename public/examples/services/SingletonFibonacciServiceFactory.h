#ifndef EXAMPLES_FIBONACCISERVICEFACTORY_H
#define EXAMPLES_FIBONACCISERVICEFACTORY_H

#include <icetray/I3ServiceFactory.h>
#include <examples/services/FibonacciService.h>

// 
//  
//
class SingletonFibonacciServiceFactory 
  : public I3ServiceFactory
{

  std::string name_;
  // this is the One Global Singleton Service we will be installing
  SequenceServicePtr singleton_service;

 public:

  virtual ~SingletonFibonacciServiceFactory() { }

  SingletonFibonacciServiceFactory(const I3Context& context) 
    : I3ServiceFactory(context)
    { 
      name_ = I3DefaultName<SequenceService>::value();
      AddParameter("name", 
		   "Where to put the FibonacciService.  Default is to  "
		   "install at the service's DefaultName",
		   name_);
    }

  void Configure()
  {
    GetParameter("name", name_);
    
    // configure gets called only once.
    singleton_service = SequenceServicePtr(new FibonacciService);
  }

  bool InstallService(I3Context& context) 
  {

    context.Put(name_, singleton_service);
    return true;
  }
};

#endif
