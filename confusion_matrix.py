import matplotlib.pyplot as plt
from ts_digi_container import *
import ROOT as r

def plot_conf_matrix(x,y):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    hist, xbins, ybins, im = ax.hist2d(x,y, bins=np.arange(-0.5,5.5,1))

    for i in range(len(ybins)-1):
        for j in range(len(xbins)-1):
            ax.text(xbins[j]+0.5,ybins[i]+0.5, hist.T[i,j], 
                    color="w", ha="center", va="center", fontweight="bold")

cont = ts_digi_container('../ldmx-sw/single_test_100k.root','LDMX_Events')
cont.get_digi_collection('trigScintDigisTag_sim')
cont.get_digi_collection('trigScintDigisUp_sim')
cont.get_digi_collection('trigScintDigisDn_sim')

threshold=50

electrons=cont.get_num_beam_electrons()
tag_hits30=cont.count_hits('trigScintDigisTag_sim',threshold)
tag_hits30_pred=np.divide(np.add(tag_hits30,1),2)

up_hits30=cont.count_hits('trigScintDigisUp_sim',threshold)
up_hits30_pred=np.divide(np.add(up_hits30,1),2)

dn_hits30=cont.count_hits('trigScintDigisDn_sim',threshold)
dn_hits30_pred=np.divide(np.add(dn_hits30,1),2)

vote=map(lambda x,y,z:np.min([x,y,z]),up_hits30_pred,tag_hits30_pred,dn_hits30_pred)

plot_conf_matrix(electrons,vote)
cont.dump(np.argwhere(np.subtract(vote,electrons)==-1).flatten())

plt.show()
