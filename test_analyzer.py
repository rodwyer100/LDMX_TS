from ts_digi_container import *
import ROOT as r

cont = ts_digi_container('../ldmx-sw/single_test_100k.root','LDMX_Events')
cont.get_digi_collection('trigScintDigisTag_sim')
cont.get_digi_collection('trigScintDigisUp_sim')
cont.get_digi_collection('trigScintDigisDn_sim')

r.gROOT.ProcessLine(".L ~/tdrstyle.C")
r.gROOT.ProcessLine("setTDRStyle()")

hist = r.TH1F("test","Title;Photo-electrons;Events",40,0,200)

for i in range(cont.tree.numentries):
    pes=cont.get_data('trigScintDigisTag_sim','pe',i)
    for pe in pes : 
        hist.Fill(pe)
    pes=cont.get_data('trigScintDigisUp_sim','pe',i)
    for pe in pes : 
        hist.Fill(pe)
    pes=cont.get_data('trigScintDigisDn_sim','pe',i)
    for pe in pes : 
        hist.Fill(pe)

hist.SetFillColor(2)
hist.SetLineColor(4)
hist.SetLineStyle(2)

hist.Draw()
