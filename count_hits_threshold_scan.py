import matplotlib.pyplot as plt
from ts_digi_container import *
import ROOT as r
from array import array

## load and initialize container
cont = ts_digi_container('test.root','LDMX_Events')
cont.get_digi_collection('trigScintDigisTag_sim')
cont.get_digi_collection('trigScintDigisUp_sim')
cont.get_digi_collection('trigScintDigisDn_sim')

accuracy=[]
threshold=[]

for th in range(0,210,10):
    threshold.append(th)

    ## get the true number of beam electrons for all events
    electrons=cont.get_num_beam_electrons()

    ## get hits from tagger array for all events and predict num. electrons
    tag_hits=cont.count_hits('trigScintDigisTag_sim',th)
    pred=np.divide(np.add(tag_hits,1),2)

    acc = np.count_nonzero(electrons==pred)/float(cont.tree.numentries)
    accuracy.append(acc)
    print "threshold:",th,"accuracy:",acc

gr=r.TGraph(len(threshold),array('f',threshold),array('f',accuracy))

can=r.TCanvas('can','can',500,500)
gr.Draw()
can.SaveAs("tresholdScan.png")
