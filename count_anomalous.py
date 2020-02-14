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


Dict = {}


## set configurable parameters
coll="TriggerPadTagger"
min_pe=2
df=pd.DataFrame(columns=["TrueData","TaggerData","UpstreamData"])

##initialize histograms
can=r.TCanvas("can","can",500,500)

hist = r.TH2F("confusion_hist",coll+";True Electrons;Pred Electrons",8,-0.5,7.5,8,-0.5,7.5)
secondaries= r.TH1D("secondaries","Secondaries Distribution;Secondaries;Events",10,0,10)

## intialize contain to read target input file
cont = ldmx_container("~whitbeck/raid/LDMX/trigger_pad_sim/Dec18/trig_scin_digi_mip_respons_10_noise_0p02.root")
cont.setup()
n=0
for i in range(cont.tin.GetEntries()):
    #if i >100: break 
    ## initialize container
    cont.getEvent(i)
    ## get true number of electrons
    true_num=cont.count_true(coll+"SimHits")
    true_num2=cont.count_true("TriggerPadUpSimHits")
    if true_num < true_num2:
        n+=1
        Dict.setdefault(i,[]).append(true_num)
        Dict.setdefault(i,[]).append(true_num2)
        Dict.setdefault(i,[]).append(cont.get_num_secondaries())
        secondaries.Fill(cont.get_num_secondaries())

print "Number of Analomous Events",n
print "\n"
print Dict
secondaries.SetFillColor(38)
secondaries.Draw()
#secondaries.GetXaxis().SetTitle( 'Min_Pe' )
#secondaries.GetYaxis().SetTitle( 'Efficiency Rate' )

can.SaveAs("strange_secondaries.png")
