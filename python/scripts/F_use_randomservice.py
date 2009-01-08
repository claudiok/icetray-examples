#!/usr/bin/env python

def main():
    """
    Simple demonstration....  you can talk to services from python,
    if those services have wrappers.  Note that there is no
    servicefactory stuff here... you call the constructor of the
    service that you want yourself.
    """

    from icecube import icetray, phys_services

    rng = phys_services.I3GSLRandomService(31334)

    print [rng.Gaus(0,1) for x in xrange(100)]


if __name__ == "__main__":
    main()
