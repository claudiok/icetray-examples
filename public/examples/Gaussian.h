#ifndef EXAMPLES_GAUSSIAN_H_INCLUDED
#define EXAMPLES_GAUSSIAN_H_INCLUDED

#include <string>
#include <vector>

//
//  A gaussian that carries it sigma and mu around with it.
//
class Gaussian 
{
  double mu_, sigma_;

 public:

  typedef double result_type;
  Gaussian(double mu, double sigma) : mu_(mu), sigma_(sigma) { }
  Gaussian() : mu_(0), sigma_(0){ }
  Gaussian(const Gaussian& g) : mu_(g.mu_), sigma_(g.sigma_) { }

  inline
  double 
  operator()(double x) const
  {
    return (1./(sigma_ * sqrt(2.0 * M_PI))) 
      * exp(-1.0 * (((x-mu_)*(x-mu_)) /  (2.0*(sigma_*sigma_))));
  }

};
#endif
