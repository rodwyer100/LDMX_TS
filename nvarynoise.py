
### change in noise ["001","002","005","01","02","05"] and plots for each number of true electrons n= 1,2,3,4

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
Noise =array("d")

stacks = []
# plot Graph
c1 = r.TCanvas( 'c1', 'c1',800,800)
c1.SetGrid()


min_pe = 2
diff_noise = ["001","002","005","01","02","05"] # 
Dict = dict()

for  noise in diff_noise:
    l=float("0."+noise)
    Noise.append(l)
    cont = ldmx_container("~whitbeck/raid/LDMX/trigger_pad_sim/Dec18/trig_scin_digi_mip_respons_10_noise_0p"+noise+".root")
    cont.setup()

    ## initialize histograms
    hist = r.TH2F("confusion_hist",coll+";True Electrons;Pred Electrons",8,-0.5,7.5,8,-0.5,7.5)
 
    for i in range(cont.tin.GetEntries()):
        #if i >1000: break
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
        hist.Fill(true_num,count_hits)
        #hist.Fill(true_num, min(count_hits,count_hits_up))
        #hist.Fill(true_num,count_clusters)
        #hist.Fill(true_num, min(count_clusters,count_clusters_up))
    
    for x in range(2,6): # four blocks in each histogram 
        values = [0.]*3
        for y in range(1,hist.GetNbinsY()+1):
            if x==y : values[0]+= hist.GetBinContent(x,y) # values on the diagonal
            if y<x : values[1] += hist.GetBinContent(x,y) # values below the diagonal
            if y>x : values[2] += hist.GetBinContent(x,y) # values above the diagonal
        total = reduce(lambda x,y : x+y, values)
        #print(total)
        event_rate = map(lambda x: (x/total), values)
        Dict.setdefault(x,[]).append(event_rate)

print Dict
print "\n"

# Initializing all the canvas

c1 = r.TCanvas( 'c1', 'c1', 1000, 1000)
c1.SetGrid()

for i in range(2,6):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,6,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])

    gr1 = r.TGraph( 6, Noise, efficiency)
    stacks.append(gr1)
    gr1.SetLineColor( i+4 )
    gr1.SetLineWidth( 4 )
    gr1.SetMarkerStyle( 21 )
    gr1.SetTitle( 'n = '+ str(i-1))
    #gr1.GetXaxis().SetNdivisions(505)
    gr1.GetXaxis().SetTitle( 'Noise' )
    gr1.GetYaxis().SetTitle( 'Efficiency Rate' )
    gr1.GetYaxis().SetRangeUser(0,1)
    #gr1.GetXaxis().SetLimits(0.000001,0.001)
    gr1.GetXaxis().SetLabelSize(0.03)
    gr1.GetYaxis().SetLabelSize(0.03)
    if i-1 == 1: gr1.Draw( 'ACP' )
    else : gr1.Draw('CP')


c1.BuildLegend(0.6,0.2,0.9,0.35,"Number of True Electrons (n):")
c1.SaveAs("ch_resp10_NoisevsEff.png")

for i in range(2,6):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,6,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])


    gr = r.TGraph( 6, Noise, under_prediction)
    stacks.append(gr)
    gr.SetLineColor( i+4 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'n = '+ str(i-1))
    #gr.GetXaxis().SetNdivisions(505)
    gr.GetXaxis().SetTitle( 'Noise ' )
    gr.GetYaxis().SetTitle( 'Under Prediction Rate' )
    gr.GetYaxis().SetRangeUser(0,1)
    #gr.GetXaxis().SetLimits(0.000001,0.001)
    gr.GetXaxis().SetLabelSize(0.03)
    gr.GetYaxis().SetLabelSize(0.03)
    if i-1 == 1: gr.Draw( 'ACP' )
    else : gr.Draw('CP')

c1.BuildLegend(0.6,0.8,0.9,0.95,"Number of True Electrons (n):")
c1.SaveAs("ch_resp10_NoisevsUnder.png")

for i in range(2,6):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,6,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])

    gr = r.TGraph(6, Noise, over_prediction)
    stacks.append(gr)
    gr.SetLineColor( i+4 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'n = '+ str(i-1))
    #gr.GetXaxis().SetNdivisions(505)
    gr.GetXaxis().SetTitle( 'Noise' )
    gr.GetYaxis().SetTitle( 'Over Prediction Rate' )
    gr.GetYaxis().SetRangeUser(0.01, 0.08)
    gr.GetXaxis().SetLabelSize(0.03)
    gr.GetYaxis().SetLabelSize(0.03)
    if i-1 == 1: gr.Draw( 'ALP' )
    else : gr.Draw('LP')

#c1.SetLogy()
c1.BuildLegend(0.25,0.65,0.55,0.8,"Number of True Electrons (n):")
c1.SaveAs("ch_resp10_NoisevsOver.png")


for i in range(2,6):
    efficiency, under_prediction, over_prediction = array("d"),array("d"),array("d")
    for x in np. arange(0,6,1):
        for y in np.arange(0,3,1):
            if y==0: efficiency.append(Dict[i][x][y])
            if y==1: under_prediction.append(Dict[i][x][y])
            if y==2: over_prediction.append(Dict[i][x][y])

    gr = r.TGraph( 6, over_prediction, efficiency)
    stacks.append(gr)
    gr.SetLineColor( i+4 )
    gr.SetLineWidth( 4 )
    gr.SetMarkerStyle( 21 )
    gr.SetTitle( 'n = '+ str(i-1))
    #gr.GetXaxis().SetNdivisions(505)
    gr.GetXaxis().SetTitle( 'Overprediction Rate' )
    gr.GetYaxis().SetTitle( 'Efficiency Rate' )
    gr.GetYaxis().SetRangeUser(0,1)
    gr.GetXaxis().SetLimits(0.01, 0.08)
    gr.GetXaxis().SetLabelSize(0.03)
    gr.GetYaxis().SetLabelSize(0.03)
    if i-1 == 1: gr.Draw( 'ALP' )
    else : gr.Draw('LP')

c1.BuildLegend(0.6,0.15,0.9,0.3,"Number of True Electrons (n):")
c1.SaveAs("ch_resp10_OvervsEff.png")












