#ifndef EXAMPLES_FIBONACCISERVICE_H
#define EXAMPLES_FIBONACCISERVICE_H

#include <examples/services/SequenceService.h>

//
// note that this class stands compeletly on its own.  It needn't
// inherit from anything, it defines a pure virtual interface to some
// "service", in this case a service that returns some sequence of
// unsigned integers.
//

class FibonacciService : public SequenceService
{

  unsigned n_;
  unsigned f_n_;
  unsigned f_n_minus_1_;

 public:

  FibonacciService() 
  { 
    n_ = 0;
    f_n_ = 1;
    f_n_minus_1_ = 0;
  }

  ~FibonacciService() { }

  virtual unsigned next() 
    {
      if (n_ == 0) 
	{ 
	  n_++;
	  return 0;
	}

      if (n_ == 1)
	{
	  n_++;
	  return 1;
	}

      // calculate next and return
      unsigned new_f_n = f_n_ + f_n_minus_1_;
      f_n_minus_1_ = f_n_;
      f_n_ = new_f_n;

      n_++;
      return f_n_;
    }

};

#endif
