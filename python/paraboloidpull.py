#!/usr/bin/python

import tables,numpy,pylab,scipy.optimize

t=tables.openFile("/Users/troy/Icecube/data/nugen_numu.000850.0000XX.h5")

def gaussian(x,p):
    return p[0] * numpy.exp ( - (x-p[1])**2/2/p[2]**2 ) + p[3]

#gaussian = lambda x,p: p[0] * numpy.exp ( - (x-p[1])**2/2/p[2]**2 ) + p[3]

def residuals(p,x,y):
    gaussian(x,p)-y

#residuals= lambda p,x,y: gaussian(x,p)-y

data, bins=numpy.histogramdd( (t.root.data.cols.I3MCTree.MaxTrack.zenith[:] - t.root.data.cols.MultiFit.zenith[:] ) /t.root.data.cols.ParaboloidFitFitParams.pbfSigmaZen[:] ,weights=t.root.data.cols.I3MCWeightDict.OneWeight[:]  ** t.root.data.cols.I3MCTree.MaxPrimary.energy[:]**-2, range=[[-5,5]], bins=50 )
bins=bins[0][:-1]

p0=[900,0,1,0]

p1,fitstatus=scipy.optimize.leastsq(residuals, p0, args=(bins,data ), maxfev=2000)

print p1

pylab.plot(bins,data,ls='steps')
pylab.plot(bins,gaussian(bins,p1))

pylab.show()
