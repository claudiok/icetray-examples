#!/usr/bin/env python

#this script creates automatically generates massive amounts of histograms

from I3Tray import *
import tables
import numpy
import pylab
import  neutrinoflux

def deltaangle(p1,p2):

    zenith1 =p1.zenith[:]
    azimuth1=p1.azimuth[:]
    zenith2 =p2.zenith[:]
    azimuth2=p2.azimuth[:]
    
    a=(numpy.sin(zenith1)  * numpy.sin(zenith2) * numpy.sin(azimuth1) * numpy.sin(azimuth2) +
       numpy.sin(zenith1)  * numpy.sin(zenith2) * numpy.cos(azimuth1) * numpy.cos(azimuth2) +
       numpy.cos(zenith1)  * numpy.cos(zenith2)
       )

    return numpy.arccos(a)

class Table:
    def __init__(self,inputfile,name=None,color='b',weight=None,weightlabel=""):
        self.name=name if name else inputfile
        self.inputfile=inputfile
        self.color=color
        self.h5file=tables.openFile(inputfile,'r')        

        if weight:
            self.weights=weight(self.GetCols())
            self.weightlabel=weightlabel
        else:
            self.weights=1
            self.weightlabel=""          

    def __del__(self):
        self.h5file.close()
        
    def GetCols(self):
        return self.h5file.root.data.cols

    def GetWeights(self):
        return self.weights
    def GetWeightLabel(self):
        return self.weightlabel
    def GetColor(self):
        return self.color
    def GetName(self):
        return self.name

class Plot:
    def __init__(self,name,function,cut=lambda x: 1,fitfunction=None,plottype=pylab.plot,bins=50,range=None,logx=False,normed=False,**kargs):
        self.name=name
        self.function=function
        self.cut=cut
        self.fitfunction=fitfunction
        self.plottype=plottype
        self.kargs=kargs
        self.bins=bins
        self.range=[range] if range else None
        self.logx=logx
        self.normed=normed
    
def WaxmanBachall(energy):
    b= 2.e-8
    return numpy.piecewise(energy,[energy  <  1.e5  , energy >  1.e7, ], [lambda x:  b / 1e5 * x**-1, lambda x: b * 1e7 * x**-3 , lambda x: b * x**-2, ])

def Atmospheric(particle):
    return ( neutrinoflux.Naumov_RQPM().GetFlux( particle.type[:], particle.energy[:], particle.zenith[:] ) + 
             neutrinoflux.Bartol()     .GetFlux( particle.type[:], particle.energy[:], particle.zenith[:] )
             )

sources = [
    Table("/data/icecube01/users/kjmeagher/processing/nugen_numu.000850.0000XX.h5","WB",'r', lambda c: c.I3MCWeightDict.OneWeight[:] / (2000.0*100/2) * WaxmanBachall(c.I3MCTree.MaxPrimary.energy[:]) ),
    Table("/data/icecube01/users/kjmeagher/processing/nugen_numu.000839.000XXX.h5","Atmospheric",'purple',lambda c: c.I3MCWeightDict.OneWeight[:] / ( 20000.0*1000/2) * Atmospheric(c.I3MCTree.MaxPrimary)),
    Table("/data/icecube01/users/kjmeagher/processing/corsika.000880.00000X.h5","Single Mu",'c', lambda c: c.CorsikaWeightMap.Weight[:]/c.CorsikaWeightMap.TimeScale[:] /10 ) ,
    Table("/data/icecube01/users/kjmeagher/processing/corsika_coincident.000920.00000X.h5","Double Mu",'g', lambda c: c.CorsikaWeightMap.Weight[:]/c.CorsikaWeightMap.TimeScale[:] /10) ,
    ]

def particle(name):
    return [  Plot(name+"Zenith" ,lambda c: eval("c."+name).zenith    [:]/I3Units.degree ,plottype=pylab.semilogy,range=[0,180] ),
              Plot(name+"Azimuth",lambda c: eval("c."+name).azimuth   [:]/I3Units.degree ,plottype=pylab.semilogy,range=[0,360]),
              #Plot(name+"X",      lambda c: eval("c."+name).position.x[:]/I3Units.degree ,plottype=pylab.semilogy,range=[-500,500]),
              #Plot(name+"Y",      lambda c: eval("c."+name).position.y[:]/I3Units.degree ,plottype=pylab.semilogy,range=[-500,500]),
              #Plot(name+"Z",      lambda c: eval("c."+name).position.z[:]/I3Units.degree ,plottype=pylab.semilogy,range=[-500,500]),
              #Plot(name+"Time",   lambda c: eval("c."+name).time      [:]/I3Units.degree ,plottype=pylab.semilogy,range=[0,1.5e6]),
              ]

def mctruth(name):
    return particle(name) + [
        Plot(name+"Energy", lambda c: numpy.log10(eval("c."+name).energy    [:] ) ,plottype=pylab.semilogy,range=[1,9]),
        ]       

def reco(name):
    return particle(name) + [
        Plot(name+"DeltaZenith" , lambda c: (eval("c."+name).zenith [:]-c.I3MCTree.MaxTrack.zenith [:])/I3Units.degree ,plottype=pylab.semilogy ,range=[-180,180]),
        Plot(name+"DeltaAzimuth" ,lambda c: (eval("c."+name).azimuth[:]-c.I3MCTree.MaxTrack.azimuth[:])/I3Units.degree ,plottype=pylab.semilogy ,range=[-360,360]),
        Plot(name+"DeltaAngle" ,  lambda c:  deltaangle(eval("c."+name),c.I3MCTree.MaxTrack)/I3Units.degree ,plottype=pylab.semilogy,range=[0,180] ),
        ]
       
def linefit(name):
    return reco(name) + [
        Plot(name+"Speed",  lambda c: eval("c."+name).speed     [:] ,plottype=pylab.semilogy,range=[0,.5]),
        ]

def cuts(name):
    return reco(name) + [
        Plot(name+"nstring",lambda c: eval("c."+name+"Cuts").nstring[:], plottype=pylab.semilogy, range=[0,40],bins=40),
        Plot(name+"ndir",lambda c: eval("c."+name+"Cuts").ndir[:], plottype=pylab.semilogy ,range=[0,300]),
        Plot(name+"ldir",lambda c: eval("c."+name+"Cuts").ldir[:], plottype=pylab.semilogy,range=[0,1000] ),
        #Plot("sdir",lambda c: eval("c."+name+"Cuts").sdir[:], plottype=pylab.semilogy ),
        ]

def gulliver(name):
    return cuts(name) + [
        Plot(name+"rlogl",lambda c: eval("c."+name+"FitParams").rlogl[:], plottype=pylab.semilogy, range=[0,70]),
        Plot(name+"ndof",lambda c: eval("c."+name+"FitParams").ndof[:], plottype=pylab.semilogy, range=[0,1000]),
        Plot(name+"logl",lambda c: eval("c."+name+"FitParams").logl[:], plottype=pylab.semilogy ,range=[0,1000]),
        Plot(name+"nmini",lambda c: eval("c."+name+"FitParams").nmini[:], plottype=pylab.semilogy,range=[0,1000] ),
        ]

def paraboloid(name):
    return gulliver(name) + [
        Plot(name+"pbfErr1",lambda c: eval("c."+name+"FitParams").pbfErr1[:], plottype=pylab.semilogy,range=[0,20]),    
        Plot(name+"pbfErr2",lambda c: eval("c."+name+"FitParams").pbfErr2[:], plottype=pylab.semilogy,range=[-20,0]),
        Plot(name+"pbfRotAng",lambda c: eval("c."+name+"FitParams").pbfRotAng[:]/I3Units.degree, plottype=pylab.semilogy,range=[0,180]),
        Plot(name+"pbfCenterLlh",lambda c: eval("c."+name+"FitParams").pbfCenterLlh[:], plottype=pylab.semilogy,range=[0,1000]),
        Plot(name+"pbfZenOff",lambda c: eval("c."+name+"FitParams").pbfZenOff[:]/I3Units.degree, plottype=pylab.semilogy,range=[-180,180]),
        Plot(name+"pbfAziOff",lambda c: eval("c."+name+"FitParams").pbfAziOff[:]/I3Units.degree, plottype=pylab.semilogy,range=[-180,180]),
        Plot(name+"pbfCurv11",lambda c: eval("c."+name+"FitParams").pbfCurv11[:], plottype=pylab.semilogy,range=[-1000,1000]),
        Plot(name+"pbfCurv12",lambda c: eval("c."+name+"FitParams").pbfCurv12[:], plottype=pylab.semilogy,range=[-1000,1000]),
        Plot(name+"pbfCurv22",lambda c: eval("c."+name+"FitParams").pbfCurv22[:], plottype=pylab.semilogy,range=[-1000,1000]),
        Plot(name+"pbfChi2",lambda c: eval("c."+name+"FitParams").pbfChi2[:], plottype=pylab.semilogy,range=[0,10]),
        Plot(name+"pbfDetCurvM",lambda c: eval("c."+name+"FitParams").pbfDetCurvM[:], plottype=pylab.semilogy,range=[-4,4]),
        Plot(name+"pbfSigmaZen",lambda c: eval("c."+name+"FitParams").pbfSigmaZen[:], plottype=pylab.semilogy,range=[-4,4]),
        Plot(name+"pbfSigmaAzi",lambda c: eval("c."+name+"FitParams").pbfSigmaAzi[:], plottype=pylab.semilogy,range=[-5,5]),
        Plot(name+"pbfCovar",lambda c: eval("c."+name+"FitParams").pbfCovar[:], plottype=pylab.semilogy,range=[-5,5]),
        Plot(name+"Sigma",lambda c: numpy.sqrt( c.ParaboloidFitFitParams.pbfSigmaZen[:]**2 +
                                                numpy.sin(c.ParaboloidFit.zenith[:])**2 *
                                                c.ParaboloidFitFitParams.pbfSigmaAzi[:]**2
                                                )/I3Units.degree,plottype=pylab.semilogy,range=[0,180] ),

        ]


cut=lambda c: ( c.MultiFit.zenith[:] > 90 *I3Units.degree )

plots = (  []
           + linefit("LineFit")
           + gulliver("SingleFit")
           + gulliver("MultiFit")
           + paraboloid("ParaboloidFit")
           + gulliver("BayesianFit")
           + mctruth("I3MCTree.MaxPrimary")
           + mctruth("I3MCTree.MaxTrack")
          )

for plot in plots:
    pylab.clf()
    print(plot.name)
    datas=[]

    for source in sources:

        if plot.logx:
            x=numpy.log10(plot.function(source.GetCols()))
        else:
            x=plot.function(source.GetCols())
        
        data,bins=numpy.histogramdd( x,weights=plot.cut(source.GetCols())*source.weights,bins=plot.bins,range=plot.range)
        bins=bins[0][:-1]

        if plot.logx:
            bins=10**bins
        if plot.normed:
            data/=sum(data)

        
        try:
            plot.plottype(bins,data,label=source.GetName(),color=source.color,linestyle='steps')
        except:
            pass
        print("\t %s %e" % (source.name, sum(data)))

        datas.append(data)

    try:
        plot.plottype(bins,sum(datas[1:]),label="Combined Sim",color='b',linewidth=2,linestyle='steps')
    except:
        pass

    pylab.legend(loc="best")
    pylab.xlabel("Rate (Hz)")
    pylab.xlabel(plot.name)
    pylab.savefig(plot.name+".png")

