#ifndef EXAMPLES_ONEPERMODULEFIBONACCISERVICEFACTORY_H_INCLUDED
#define EXAMPLES_ONEPREMODULEFIBONACCISERVICEFACTORY_H_INCLUDED

#include <icetray/I3ServiceFactory.h>
#include <examples/services/FibonacciService.h>

// 
//  
//
class OnlyOneModuleFibonacciServiceFactory 
  : public I3ServiceFactory
{
  std::string modulename_;
  std::string servicename_;

 public:

  virtual ~OnlyOneModuleFibonacciServiceFactory() { }

  OnlyOneModuleFibonacciServiceFactory(const I3Context& context) 
    : I3ServiceFactory(context)
    { 
      modulename_ = "unspecified";
      AddParameter("modulename",
		   "which module to install this service for",
		   modulename_);

      servicename_ = "unspecified";
      AddParameter("servicename",
		   "which name to install this service under",
		   servicename_);
    }

  void Configure()
  {
    GetParameter("modulename", modulename_);
    GetParameter("servicename", servicename_);
  }

  bool InstallService(I3Context& context) 
  {
    // the name of the instance of the object is inside the
    // configuration, which is inside the context.
    if (context.Get<I3Configuration>().InstanceName() != modulename_)
      return false;

    SequenceServicePtr singleton_service(new FibonacciService);

    // this will install under the SequenceService's DefaultName
    context.Put(servicename_, singleton_service);
    return true;
  }
};

#endif
