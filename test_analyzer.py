from ts_digi_container import *
import ROOT as r

## initialize container
#cont = ts_digi_container('../ldmx-sw/single_test_100k.root','LDMX_Events')
cont = ts_digi_container('test.root','LDMX_Events')
cont.get_digi_collection('trigScintDigisTag_sim')
cont.get_digi_collection('trigScintDigisUp_sim')
cont.get_digi_collection('trigScintDigisDn_sim')

## configuration for pretty root plots
r.gROOT.ProcessLine(".L tdrstyle.C")
r.gROOT.ProcessLine("setTDRStyle()")

## initialize root histogram
hist = r.TH1F("test","Title;Photo-electrons;Events",40,0,200)

## loop over events
for i in range(cont.tree.numentries):
    ## get list of pe for tagger array for event i
    pes=cont.get_data('trigScintDigisTag_sim','pe',i)
    for pe in pes : 
        hist.Fill(pe)
    ## get list of pe for upstream array for event i
    pes=cont.get_data('trigScintDigisUp_sim','pe',i)
    for pe in pes : 
        hist.Fill(pe)
    ## get list of pe for downstream array for event i
    pes=cont.get_data('trigScintDigisDn_sim','pe',i)
    for pe in pes : 
        hist.Fill(pe)

#plot!
c1 = r.TCanvas("c1", "hist canvas", 600,  500)
hist.SetFillColor(2)
hist.SetLineColor(4)
hist.SetLineStyle(2)
hist.Draw()

c1.SaveAs( hist.GetName()+".png")
