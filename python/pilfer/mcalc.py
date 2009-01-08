#!/usr/bin/python

from math import e

class Calculator :

    def __init__(self,accuracy = 10,conflevel = 0.9,discovery = 5.73e-7) :
        self.__conflevel = conflevel
        self.__discovery = discovery
        self.__accuracy = accuracy
        self.__lastnObs = 0
        self.__lastnu = 0
        self.__facdict = {}
        self.__facdict[0] = 1
        self.__facdict[1] = 1
   
    def set_conflevel(self,conflevel) :
        self.__conflevel = conflevel

    def set_accuracy(self,accuracy) :
        self.__accuracy = accuracy

    def set_discovery(self,discovery) :
        self.__discovery = discovery

    def fac(self,x) :
        if self.__facdict.keys().count(x) != 0 : return self.__facdict[x]
        if x > 1 :
            # print "------------------Calculating Factorial of " + str(x)
            toreturn = x * self.fac(x-1)
            self.__facdict[x] = toreturn
            return toreturn
        else : return 1

    def poisson(self,sigma, n) :
        # print "Poisson: " + str(sigma) + " " + str(n)
        # print str(sigma) + " " + str(n)
        x = sigma**n * e**-sigma / float(self.fac(n))
        # print x
        return x

    def least_detectable_signal(self,nback) :
        n = 0
        sum = self.poisson(nback,n)
        while 1 - sum > self.__discovery :
            n += 1
            sum += self.poisson(nback,n)
        ncritical = n + 1
        # print "ncritical = " + str(ncritical)
        
        stepsize = 1 / float(self.__accuracy)
        ntot = ncritical
        sum = 1
        while sum > (1 - self.__conflevel) :
            ntot += stepsize
            sum = 0
            #print "----"
            for n in range(ncritical) :
                #print n
                sum += self.poisson(ntot,n)
            # print "ntot = " + str(ntot) + " sum = " + str(sum)
        #print "ntot = " + str(ntot)

        lds = ntot - nback
        return lds

    def average_upper_limit(self,expBack,conflevel = 0.9) :
        self.__conflevel = conflevel
        self.__lastnObs = 0
        self.__lastnu  = 0
        avgUppLim = 0
        nObs = 0
        calculate = True
        while calculate :
            upper = self.__upper_confidence_interval(nObs,expBack)
            weight = self.poisson(expBack,nObs)
            avgUppLim += upper * weight
            # print "Outer loop: nObs: " + str(nObs) + " upper: " + str(upper) + " weight: " + str(weight)
            nObs += 1
            if(upper * weight / avgUppLim < .00005 ) : calculate = False
            
        return avgUppLim

    def __upper_confidence_interval(self,nObs,expBack) :
        from math import floor
        nu = 0
        if nObs > self.__lastnObs : nu = self.__lastnu
        cupper = -1
        firstpass = True
        while cupper < 0 :
            alower, aupper = self.__acceptance_interval(nu,expBack)
            if firstpass and alower > nObs : print "did it **************"
            # print "Middle Loop: nu: " + str(nu) + " lower: " + str(alower) + " upper: " + str(aupper) + " nObs: " + str(nObs)
            if alower > nObs : cupper = nu
            nu += 1 / float(self.__accuracy)
            firstpass = False

        self.__lastnObs = nObs
        self.__lastnu = floor(nu - 5 / float(self.__accuracy))
        if self.__lastnu < 0 : self.__lastnu = 0
        return cupper

    def __acceptance_interval(self, nu, expBack) :
        nObs = 0
        pTot = 0
        rDict = {}
        calculate = True
        while calculate :
            # print "First Inner Loop: nObs: " + str(nObs) + " expBack: " + str(expBack) + " nu: " + str(nu)
            p = self.poisson(expBack + nu,nObs)
            pbest = 0
            if nObs < expBack : pbest = self.poisson(expBack,nObs)
            else : pbest = self.poisson(nObs,nObs)
            ratio = p / pbest
            if rDict.keys().count(ratio) > 0 : rDict[ratio + .00000001] = [p,nObs]
            else : rDict[ratio] = [p,nObs]
            nObs += 1
            pTot += p
            # print "First Inner Loop Result: pTot: " + str(pTot) + " ratio: " + str(ratio)
            if pTot > 0.99999 or (1.0 - self.__conflevel) / (1.0 - pTot) > 5 :
                calculate = False
            
        alower = -1
        aupper = -1
        pTot = 0
        for ratio in reversed(sorted(rDict.keys())) :
            
            if pTot == 0 :
                alower = rDict[ratio][1]
                aupper = rDict[ratio][1]
            pTot += rDict[ratio][0]
            if rDict[ratio][1] < alower : alower = rDict[ratio][1]
            if rDict[ratio][1] > aupper : aupper = rDict[ratio][1]
            # print "Second Inner Loop: ratio: " + str(ratio) + " nObs: " + str(rDict[ratio][1]) + " pTot: " + str(pTot)
            if pTot > self.__conflevel : break

        if pTot < self.__conflevel and nu != 0 :
            print "mrfCalculator: Did not complete enough calculations.  Your answer could be wrong.  pTot: " + str(pTot) + " nu: " + str(nu) + " expBack: " + str(expBack) + " alower: " + str(alower) + " aupper: " + str(aupper)
        return alower, aupper
