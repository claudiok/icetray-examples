#!/usr/bin/env python

def rootlogon() :
    from ROOT import gROOT, gStyle, kBlue, kWhite, kBlack
    
    gROOT.SetBatch(1)  # A 1 here turns off graphics, 0 keeps them on
    
    gROOT.SetStyle("Plain")
    gStyle.SetOptStat(0) # 1 turns on the stat box, 0 turns it off
    gStyle.SetOptFit(0)  # Refer to the above url both of these
    # parameters are actually responsible for
    # for a number of different behaviors.
    
    gStyle.SetCanvasBorderMode(0)
    gStyle.SetPadBorderMode(0)
    
    gStyle.SetStatBorderSize(1)    # A border size 0 gives no border at all
    gStyle.SetTitleBorderSize(0)   # 1 gives just a line, and ( > 1) gives
    # the infamous 3-D shadow effect
    
    gStyle.SetTextFont(132)         # Times Roman Font
    gStyle.SetLabelFont(132,"XYZ")  # This sets all 3 axis labels
    gStyle.SetTitleFont(132, "XYZ") # This sets all 3 axis titles
    gStyle.SetTitleFont(132, "0")   # This sets the main pad title
    gStyle.SetStatFont(132)         # This sets the stat box
    
    gStyle.SetHistLineWidth(2)      # Use bold lines
    gStyle.SetHistLineColor(kBlue)
    
    gStyle.SetPadColor(kWhite)
    gStyle.SetCanvasColor(kWhite)
    gStyle.SetTitleColor(kBlack, "XYZ")
    
    gStyle.SetLabelSize(0.04, "XYZ")      # Size of numbers on axes
    gStyle.SetTitleSize(0.05, "XYZ")      # Size of Titles on axes
    gStyle.SetTitleSize(0.08, "0")        # Size of main pad title
    
    gStyle.SetStatFontSize(0.04)  # Size of text in stat box.  Note that this
    # is a good way to control the box size, as well
    
    gStyle.SetPadTickX(1)  # Set this to 1 for unlabeled top axis, 2 for labeled
    gStyle.SetPadTickY(1)  # Set this to 1 for unlabeled right axis, 2 for labeled
    
    gStyle.SetGridStyle(3) # You can get a solid line with 1 or a dotted with 3
    gStyle.SetGridWidth(1)
    
    gStyle.SetPadGridX(0)     # 1 turns on the grid, 0 turns it off
    gStyle.SetPadGridY(0)
    
    #   gStyle.SetMarkerStyle(20)  # 3 is a star, try 8 for a scaleable dot
    gStyle.SetMarkerStyle(8)  # 3 is a star, try 8 for a scaleable dot
    gStyle.SetMarkerSize(0.3)
    
    gStyle.SetPadBottomMargin(0.1)  # Control margin size, default is 0.1
    gStyle.SetPadTopMargin(0.1)
    gStyle.SetPadLeftMargin(0.1)
    gStyle.SetPadRightMargin(0.1)
    
    gStyle.SetCanvasDefH(480) # No need to resize your canvas every time,
    gStyle.SetCanvasDefW(640) # or even pass the size arguments to the
    gStyle.SetCanvasDefX(10)  # constructor!
    gStyle.SetCanvasDefY(10)
    
    gStyle.SetPalette(1) # pretty colors rather than the ugly default
    
    gROOT.ForceStyle()  # By default, gStyle only applies to new objects being
    # created.  This also applies it to objects being read
    # from a file.  Note that objects already in memory
    # will not be affected by gStyle at all.
    
def fitstyle() :
    from ROOT import gROOT, gStyle, kBlue, kWhite, kBlack

    gROOT.SetBatch(1)  # A 1 here turns off graphics, 0 keeps them on

    gROOT.SetStyle("Plain")
    gStyle.SetOptStat(110) # 1 turns on the stat box, 0 turns it off
    gStyle.SetOptFit(1)  # Refer to the above url both of these
    # parameters are actually responsible for
    # for a number of different behaviors.
    
    gStyle.SetCanvasBorderMode(0)
    gStyle.SetPadBorderMode(0)
    
    gStyle.SetStatBorderSize(1)    # A border size 0 gives no border at all
    gStyle.SetTitleBorderSize(0)   # 1 gives just a line, and ( > 1) gives
    # the infamous 3-D shadow effect
    
    gStyle.SetTextFont(132)         # Times Roman Font
    gStyle.SetLabelFont(132,"XYZ")  # This sets all 3 axis labels
    gStyle.SetTitleFont(132, "XYZ") # This sets all 3 axis titles
    gStyle.SetTitleFont(132, "0")   # This sets the main pad title
    gStyle.SetStatFont(132)         # This sets the stat box
    
    gStyle.SetHistLineWidth(2)      # Use bold lines
    gStyle.SetHistLineColor(kBlue)
    
    gStyle.SetPadColor(kWhite)
    gStyle.SetCanvasColor(kWhite)
    gStyle.SetTitleColor(kBlack, "XYZ")

    gStyle.SetLabelSize(0.04, "XYZ")      # Size of numbers on axes
    gStyle.SetTitleSize(0.05, "XYZ")      # Size of Titles on axes
    gStyle.SetTitleSize(0.08, "0")        # Size of main pad title
    
    gStyle.SetStatFontSize(0.04)  # Size of text in stat box.  Note that this
    # is a good way to control the box size, as well
    
    gStyle.SetPadTickX(1)  # Set this to 1 for unlabeled top axis, 2 for labeled
    gStyle.SetPadTickY(1)  # Set this to 1 for unlabeled right axis, 2 for labeled
    
    gStyle.SetGridStyle(3) # You can get a solid line with 1 or a dotted with 3
    gStyle.SetGridWidth(1)
    
    gStyle.SetPadGridX(0)     # 1 turns on the grid, 0 turns it off
    gStyle.SetPadGridY(0)
    
    #   gStyle.SetMarkerStyle(20)  # 3 is a star, try 8 for a scaleable dot
    gStyle.SetMarkerStyle(8)  # 3 is a star, try 8 for a scaleable dot
    gStyle.SetMarkerSize(0.3)
    
    gStyle.SetPadBottomMargin(0.1)  # Control margin size, default is 0.1
    gStyle.SetPadTopMargin(0.1)
    gStyle.SetPadLeftMargin(0.1)
    gStyle.SetPadRightMargin(0.1)
    
    gStyle.SetCanvasDefH(480) # No need to resize your canvas every time,
    gStyle.SetCanvasDefW(640) # or even pass the size arguments to the
    gStyle.SetCanvasDefX(10)  # constructor!
    gStyle.SetCanvasDefY(10)
    
    gStyle.SetPalette(1) # pretty colors rather than the ugly default
    
    gROOT.ForceStyle()  # By default, gStyle only applies to new objects being
    # created.  This also applies it to objects being read
    # from a file.  Note that objects already in memory
    # will not be affected by gStyle at all.
    
def rootcolorsindex(index) :
    from ROOT import kBlue,kRed,kGreen,kCyan,kMagenta,kYellow,kAzure,kPink,kSpring,kViolet,kOrange,kTeal
    colors = [kBlue,kRed,kGreen,kCyan,kMagenta,kYellow,kPink,kSpring,kViolet,kAzure,kOrange,kTeal]
    index = index % len(colors)
    return colors[index]

def list2ROOT(list,name,title,nbins,minx,maxx) :
    from ROOT import TH1F
    hist = TH1F(name,title,nbins,minx,maxx)
    if len(list) == 0 : return hist
    if type(list[0]) == tuple :
        for item in list : hist.Fill(item[0],item[1])
    else :
        for item in list : hist.Fill(item)
    return hist

def lists2ROOT(list,weights,name,title,nbins,minx,maxx) :
    if len(list) != len(weights) :
        print("List of weights should be as long as list of values.")
        return False

    from ROOT import TH1F
    hist = TH1F(name,title,nbins,minx,maxx)
    for i in range(len(list)) : hist.Fill(list[i],weights[i])
    return hist

def hists2stack(dict,path = "",norm = "",scale = "",tlegend = None) :
    from os.path import split,splitext
    from ROOT import THStack,TLegend,kWhite

    firsthist = list(dict.values())[0]
    stack = THStack(firsthist.GetTitle().split()[0] + "stack",firsthist.GetTitle())
    legend = None
    if tlegend == None : legend = TLegend(0.8,0.85,1.0,1.0)
    else : legend = TLegend(tlegend[0],tlegend[1],tlegend[2],tlegend[3])
    legend.SetFillColor(kWhite)
    normstack = THStack(firsthist.GetTitle().split()[0] + "normstack",firsthist.GetTitle())
    normlegend = None
    if tlegend == None : normlegend = TLegend(0.8,0.85,1.0,1.0)
    else : normlegend = TLegend(tlegend[0],tlegend[1],tlegend[2],tlegend[3])
    normlegend.SetFillColor(kWhite)

    istream = 0
    for stream, hist in sorted(dict.items()) :
        hist.SetLineColor(rootcolorsindex(istream))
        legend.AddEntry(hist,stream)
        stack.Add(hist)

        normhist = hist.Clone(hist.GetTitle().split()[0] + "norm")
        scalefactor = 0
        if normhist.Integral() != 0 : scalefactor = 1/float(normhist.Integral())
        normhist.Scale(scalefactor)
        normlegend.AddEntry(normhist,stream)
        normstack.Add(normhist)

        istream += 1
        
    if path != "" :
        from ROOT import TCanvas
        base,filename = split(path)
        if not base == "" : base += "/"
        basefile,ext = splitext(filename)

        c1 = TCanvas("defaultcanvas",firsthist.GetTitle())
        stack.Draw("nostack")
        legend.Draw()
        c1.SetLogy(False)
        stack.GetXaxis().SetTitle(firsthist.GetXaxis().GetTitle())
        stack.GetYaxis().SetTitle(firsthist.GetYaxis().GetTitle())
        if (not norm == "norm") and (not scale == "log") : c1.Print(base + basefile + ".scale.linear" + ext)
        c1.SetLogy(True)
        stack.GetXaxis().SetTitle(firsthist.GetXaxis().GetTitle())
        stack.GetYaxis().SetTitle(firsthist.GetYaxis().GetTitle())
        if (not norm == "norm") and (not scale == "linear") : c1.Print(base + basefile + ".scale.log" + ext)
        
        normstack.Draw("nostack")
        normlegend.Draw()
        c1.SetLogy(False)
        normstack.GetXaxis().SetTitle(firsthist.GetXaxis().GetTitle())
        normstack.GetYaxis().SetTitle(firsthist.GetYaxis().GetTitle())
        if (not norm == "scale") and (not scale == "log") : c1.Print(base + basefile + ".norm.linear" + ext)
        c1.SetLogy(True)
        normstack.GetXaxis().SetTitle(firsthist.GetXaxis().GetTitle())
        normstack.GetYaxis().SetTitle(firsthist.GetYaxis().GetTitle())
        if (not norm == "scale") and (not scale == "linear") : c1.Print(base + basefile + ".norm.log" + ext)
        del c1

    return {"stack" : stack,
            "legend" : legend,
            "normstack" : normstack,
            "normlegend" : normlegend}

def cumHist(hist,fraction = True) :
    from ROOT import TH1F
    newhist = TH1F(hist.GetName() + "_cum",hist.GetTitle() + "_cum",
                   hist.GetNbinsX(),hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())

    if fraction :
        sum = 0.0
        newsum = 0.0
        for i in range(hist.GetNbinsX()+1) : sum += hist.GetBinContent(i)
        for i in range(hist.GetNbinsX()+1) :
            newsum += hist.GetBinContent(i)
            newhist.SetBinContent(i,newsum/sum)
    else :
        sum = 0.0
        for i in range(hist.GetNbinsX()+1) :
            sum += hist.GetBinContent(i)
            newhist.SetBinContent(i,sum)

    return newhist

def printhist(hist,filename,logy = True) :
    from ROOT import TCanvas
    c1 = TCanvas("defaultcanvas",hist.GetTitle())
    hist.Draw()
    c1.SetLogy(logy)
    c1.Print(filename)
    del c1
