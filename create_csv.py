# this code writes some ROOT data to a csv file.


import ROOT as r
from ts_digi_container import *
import csv
import numpy as np
from array import array 

r.gStyle.SetOptStat(0)
r.gROOT.ProcessLine(".L tdrstyle.C")
r.gROOT.ProcessLine("setTDRStyle()")
r.gROOT.SetBatch(True)

anamolous=[]
TrueData = []
TwoArrayData=[]
TaggerData = []
UpstreamData = []

## set configurable parameters
coll="TriggerPadTagger" 


## intialize contain to read target input file
cont = ts_digi_container("~whitbeck/raid/LDMX/trigger_pad_sim/Dec18/trig_scin_digi_mip_respons_10_noise_0p02.root")
cont.setup()


for i in range(cont.tin.GetEntries()):
    if i > 5: break    
    ## initialize container
    cont.getEvent(i)
    ## get true number of electrons
    true_num=cont.count_true(coll+"SimHits")
    true_num2=cont.count_true("TriggerPadUpSimHits")    
    

    TaggerPe = np.array(cont.trigger_pad_pe(coll+"Digi"))
    for xi,x in enumerate(TaggerPe) : # removing odd data from tagger data
        if x < 0 or np.isinf(x) or np.isnan(x) :
            TaggerPe[xi]=0
    TaggerPe = map(int,TaggerPe) # orginally stores as float
    #print(type(TaggerPe))
    UpstreamPe= np.array(cont.trigger_pad_pe("TriggerPadUpDigi"))
    for xi,x in enumerate(UpstreamPe) : # removing odd data from Upstream array
        if x < 0 or np.isinf(x) or np.isnan(x) :
            UpstreamPe[xi]=0
    UpstreamPe = map(int,UpstreamPe)
    #print(len(UpstreamPe))

    #print "- - - - - - - - - - event: ",i," - - - - - - - - - - - "
    # factor into this there are are several events for which 
    if true_num2 <= true_num:
        TrueData.append(true_num)
        TaggerData.append(TaggerPe)
        UpstreamData.append(UpstreamPe)
        TwoArrayData.append(np.concatenate((TaggerPe,UpstreamPe),axis = None))

with open("ldmxdata.csv","w") as f:
    thewriter = csv.writer(f)
    thewriter.writerow(["TaggerPe","UpstreamPe","label"])
    for i in range(len(TrueData)):
        thewriter.writerow([TaggerData[i],UpstreamData[i],TrueData[i]])
  
