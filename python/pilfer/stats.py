import scipy.stats, scipy.optimize

def LeastDetectableSignal(mub,sigma=5,cl=0.90):
    #five sigma = 5.73303143847e-07
    alpha=2*(1-scipy.stats.norm.cdf(sigma))
    lncl=cl

    ncrit=0
    while scipy.stats.poisson.sf(ncrit,mub) > alpha:
        ncrit+=1

    mu=scipy.optimize.fsolve(lambda x:scipy.stats.poisson.sf(ncrit,x)-cl,ncrit)

    return ncrit+1,mu-mub

#print LeastDetectableSignal(3.0)
