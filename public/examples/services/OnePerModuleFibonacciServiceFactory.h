#ifndef EXAMPLES_ONEPERMODULEFIBONACCISERVICEFACTORY_H_INCLUDED
#define EXAMPLES_ONEPERMODULEFIBONACCISERVICEFACTORY_H_INCLUDED

#include <icetray/I3ServiceFactory.h>
#include <examples/services/FibonacciService.h>

// 
//  
//
class OnePerModuleFibonacciServiceFactory 
  : public I3ServiceFactory
{
 public:

  virtual ~OnePerModuleFibonacciServiceFactory() { }

  OnePerModuleFibonacciServiceFactory(const I3Context& context) 
    : I3ServiceFactory(context)
    { 
    }

  void Configure()
  {
  }

  bool InstallService(I3Context& context) 
  {
    // for every context we create a new service and add it
    SequenceServicePtr singleton_service(new FibonacciService);

    // this will install under the SequenceService's DefaultName
    context.Put(singleton_service);
    return true;
  }
};

#endif
