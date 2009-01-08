from icecube import icetray, dataclasses
from icecube.phys_services import I3RandomService

class ConstantService(I3RandomService):
    """
    Dummy example implementation of a service.  Implements
    I3RandomService but actually just supplies a constant no matter
    what it is asked.
    """
    
    def __init__(self, value):
        I3RandomService.__init__(self)
        self.value = value

    def Binomial(self, ntot, prob):
        return self.value

    def Exp(self, tau):
        return self.value

    def Integer(self, imax):
        return self.value

    def Poisson(self, x1):
        return self.value

    def PoissonD(self, x1, x2):
        return self.value

    def Gaus(self, mean, stddev):
        return self.value

    
