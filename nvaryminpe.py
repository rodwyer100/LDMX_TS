### change in min_pe 1-10 and plots for each number of true electrons n= 1,2,3,4

import ROOT as r
from ldmx_container import *
import pandas as pd
import numpy as np
from array import array
r.gStyle.SetOptStat(0)
r.gROOT.ProcessLine(".L ~/tdrstyle.C")
r.gROOT.ProcessLine("setTDRStyle()")
r.gROOT.SetBatch(True)


## set configurable parameters
coll="TriggerPadTagger" #other options: "TriggerPadUpSimHits", "TriggerPadDownSimHits"

## intialize contain to read target input file
cont = ldmx_container("~whitbeck/raid/LDMX/trigger_pad_sim/Dec18/trig_scin_digi_mip_respons_10_noise_0p001.root")
cont.setup()

stacks = [] # to keep hist in memory 


Dict= dict()
Minpes = array("d")

for min_pe in np.arange(1.0,11.0,1.0):
    Minpes.append(min_pe)

    ## initialize histograms
    
    hist = r.TH2F("confusion_hist",coll+";True Electrons;Pred Electrons",8,-0.5,7.5,8,-0.5,7.5)
 
    for i in range(cont.tin.GetEntries()):
        if i>100: break
        ## initialize container
        cont.getEvent(i)

        ## get true number of electrons
        true_num=cont.count_true(coll+"SimHits")

        #### ALGORITHM 1: COUNT THE NUMBER HITS IN AN ARRAY
        count_hits=cont.count_hits(coll+"Digi",min_pe)
        count_hits_up=cont.count_hits("TriggerPadUpDigi",min_pe)
    
        #### ALGORITHM 2: COUNT THE NUMBER OF HIT CLUSTERS
        count_clusters=cont.count_clusters(coll+"Digi",min_pe)
        count_clusters_up=cont.count_clusters("TriggerPadUpDigi",min_pe)

        ## fill histograms 

        #hist.Fill(true_num,count_hits)
        #hist.Fill(true_num, min(count_hits,count_hits_up))
        #hist.Fill(true_num,count_clusters)
        hist.Fill(true_num, min(count_clusters,count_clusters_up))
        
    for x in range(2,6): # four blocks in each histogram; x and y represent the histogram block number
        values = [0]*3 #three variable list [eff,under,over] 
        for y in range(1,hist.GetNbinsY()+1):     # 8 y's
            if x==y : values[0] += hist.GetBinContent(x,y) # values on the diagonal
            if y<x  : values[1] += hist.GetBinContent(x,y) # values below the diagonal
            if y>x  : values[2] += hist.GetBinContent(x,y) # values above the diagonal
   
 
        #print "values", values
        total = reduce(lambda x,y : x+y, values)
        #print "total", total
        event_rate = map(lambda x: (x/total), values)
        #print "event_rate", event_rate
        Dict.setdefault(x,[]).append(event_rate)
#NOTE: All the dict keywords are +1 the number of true electrons
# Initializing all the canvas

c1 = r.TCanvas( 'c1', 'c1', 1000, 1000)
c1.SetGrid()

print "1:", Dict[2]
print "\n"
print "2",Dict[3]
print "\n"
print "3",Dict[4]
print "\n"
print "4", Dict[5]
print "\n"

for i in range(5,1,-1):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,10,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])

    print "overprediction", over_prediction
    print "efficiency", efficiency
    print "\n"
    maximum  =  Dict[2][0][2]
    minimum = Dict[5][9][2]
    print "mas,min", maximum, minimum
    print "\n"
    gr = r.TGraph( 10, Minpes, over_prediction)
    stacks.append(gr)
    gr.SetLineColor( i+4 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'n = '+ str(i-1))
    #gr.GetXaxis().SetNdivisions(505)
    gr.GetXaxis().SetTitle( 'Min_Pe' )
    gr.GetYaxis().SetTitle( 'Over Prediction Rate' )
    #gr.GetYaxis().SetRangeUser(minimum, maximum)
    #gr.GetXaxis().SetLimits(0.0001,11)
    gr.GetXaxis().SetLabelSize(0.03)
    gr.GetYaxis().SetLabelSize(0.03)
    if i-1 == 4: gr.Draw( 'ALP' )
    else : gr.Draw('LP')

#c1.SetLogy()
#c1.SetLogx()
c1.BuildLegend(0.65,0.75,0.95,0.9,"Number of True Electrons (n):")
c1.SaveAs("a..mincc_response20_MinPevsOver.png")

for i in range(5,1,-1):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,10,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])

    
    gr = r.TGraph( 10, Minpes, under_prediction)
    stacks.append(gr)
    gr.SetLineColor( i+4 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'n = '+ str(i-1))
    #gr.GetXaxis().SetNdivisions(505)
    gr.GetXaxis().SetTitle( 'Min_Pe' )
    gr.GetYaxis().SetTitle( 'Over Prediction Rate' )
    gr.GetYaxis().SetRangeUser(0, 1)
    #gr.GetXaxis().SetLimits(0.0001,11)
    gr.GetXaxis().SetLabelSize(0.03)
    gr.GetYaxis().SetLabelSize(0.03)
    if i-1 == 4: gr.Draw( 'ALP' )
    else : gr.Draw('LP')

#c1.SetLogy()
#c1.SetLogx()
c1.BuildLegend(0.65,0.75,0.95,0.9,"Number of True Electrons (n):")
c1.SaveAs("a..mincc_response20_MinPevsOver.png")


for i in range(5,1,-1):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,10,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])
    
    print "overprediction", over_prediction
    print "efficiency", efficiency
    print "\n"
    maximum  =  Dict[2][0][2]
    minimum = Dict[5][9][2]
    print "mas,min", maximum, minimum 
    print "\n"
    gr = r.TGraph( 10, Minpes, over_prediction)
    stacks.append(gr)
    gr.SetLineColor( i+4 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'n = '+ str(i-1))
    #gr.GetXaxis().SetNdivisions(505)
    gr.GetXaxis().SetTitle( 'Min_Pe' )
    gr.GetYaxis().SetTitle( 'Over Prediction Rate' )
    #gr.GetYaxis().SetRangeUser(minimum, maximum)
    #gr.GetXaxis().SetLimits(0.0001,11)
    gr.GetXaxis().SetLabelSize(0.03)
    gr.GetYaxis().SetLabelSize(0.03)
    if i-1 == 4: gr.Draw( 'ALP' )
    else : gr.Draw('LP')

#c1.SetLogy()
#c1.SetLogx()
c1.BuildLegend(0.65,0.75,0.95,0.9,"Number of True Electrons (n):")
c1.SaveAs("a..mincc_response20_MinPevsOver.png")


for i in range(5,1,-1):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,10,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])

    print type(efficiency) 
    maximum  =  Dict[2][0][2]
    print "Max", maximum
    minimum = Dict[5][9][2]
    gr = r.TGraph( 10, over_prediction, efficiency )
    stacks.append(gr)
    gr.SetLineColor( i+4 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'n = '+ str(i-1))
    gr.GetXaxis().SetNdivisions(505)
    gr.GetXaxis().SetTitle( 'Overprediction Rate' )
    gr.GetYaxis().SetTitle( 'Efficiency Rate' )
    gr.GetYaxis().SetRangeUser(0,1)
    #gr.GetXaxis().SetRangeUser(minimum, 0.07)
    gr.GetXaxis().SetLabelSize(0.03)
    gr.GetYaxis().SetLabelSize(0.03)
    if i-1 == 4: gr.Draw( 'ALP' )
    else : gr.Draw('LP')

#c1.SetLogx()
#c1.SetLogy()
c1.BuildLegend(0.2,0.75,0.5,0.9,"Number of True Electrons (n):")
c1.SaveAs("a..miincc_response20_OvervsEff.png")

