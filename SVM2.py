# basic support vector machine algorithm; using sklearn modules


import ROOT as r
from ldmx_container import *
import pandas as pd
from sklearn import svm
import numpy as np
from array import array 
r.gStyle.SetOptStat(0)
r.gROOT.ProcessLine(".L ~/tdrstyle.C")
r.gROOT.ProcessLine("setTDRStyle()")
r.gROOT.SetBatch(True)

anamolous=[]
TrueData = []
TwoArrayData=[]
TaggerData = []
UpstreamData = []

## set configurable parameters
coll="TriggerPadTagger" 
min_pe=2


##initialize histograms
hist = r.TH2F("confusion_hist",coll+";True Electrons;Pred Electrons",8,-0.5,7.5,8,-0.5,7.5)
hist_true = r.TH1F("true_hist",coll+";True Electrons",8,-0.5,7.5)

## intialize contain to read target input file
cont = ldmx_container("~whitbeck/raid/LDMX/trigger_pad_sim/Dec18/trig_scin_digi_mip_respons_10_noise_0p02.root")
cont.setup()
n=0
for i in range(cont.tin.GetEntries()):
    if i >1000: break 
    
    ## initialize container
    cont.getEvent(i)
    ## get true number of electrons
    true_num=cont.count_true(coll+"SimHits")
    true_num2=cont.count_true("TriggerPadUpSimHits")    
    TaggerPe = np.array(cont.trigger_pad_pe(coll+"Digi"))
    for xi,x in enumerate(TaggerPe) :
        if x < 0 or np.isinf(x) or np.isnan(x) :
            TaggerPe[xi]=0
    TaggerPe = map(int,TaggerPe)
    UpstreamPe= np.array(cont.trigger_pad_pe("TriggerPadUpDigi"))
    for xi,x in enumerate(UpstreamPe) :
        if x < 0 or np.isinf(x) or np.isnan(x) :
            UpstreamPe[xi]=0
    UpstreamPe = map(int,UpstreamPe)
    print "- - - - - - - - - - event: ",i," - - - - - - - - - - - "
    if true_num2<=true_num:
        TrueData.append(true_num)
        TaggerData.append(TaggerPe)
        UpstreamData.append(UpstreamPe)
        TwoArrayData.append(np.concatenate((TaggerPe,UpstreamPe),axis = None))
    else: 
        anamolous.append(i)


trialnum = int(len(TrueData)*0.1) # spliting 10% of data into trial set;int just truncates the decimal part

for c in np.arange(-10,11,1):
    clf2 =  svm.SVC(C= 2.0**c, kernel='linear')
    x,y= TaggerData[:-trialnum],TrueData[:-trialnum] # alternatively: x,y= TwoArrayData[:-trialnum],TrueData[:trialnum]
    clf2.fit(x,y)

    for i in np.arange(1,trialnum,1): # testing data
        print "Test",i
        print "true num",TrueData[-i] 
        pred =  clf2.predict([TaggerData[-i]]) # alternatively: clf.predict([TwoArrayData[-i]])
        print "Prediction", pred[0]
        hist.Fill(TrueData[-i], pred[0] )
        hist_true.Fill(TrueData[-i])
    
    print "\n"
    ## normalize each num_true electrons column to same area
    for x in range(1,hist.GetNbinsX()+1):
        for y in range(1,hist.GetNbinsY()+1):
            if hist_true.GetBinContent(x) != 0 :
                hist.SetBinContent(x,y,hist.GetBinContent(x,y)/hist_true.GetBinContent(x))


    ## plot histograms
    can=r.TCanvas("can","can",500,500)
    can.SetRightMargin(0.15)
    hist.Draw("colz,text")
    leg = r.TLegend(.2,.7,.5,.9, "Trial Dataset; C:2^"+str(c))
    leg.SetBorderSize(0)
    leg.Draw()
    can.SaveAs("SVM_Tagger"+str(c)+".png")


