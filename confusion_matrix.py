import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from ts_digi_container import *
import ROOT as r

## formatting/plotting confusion matrix in pyplot
def plot_conf_matrix(x,y):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    hist, xbins, ybins, im = ax.hist2d(x,y, bins=np.arange(-0.5,5.5,1))

    for i in range(len(ybins)-1):
        for j in range(len(xbins)-1):
            ax.text(xbins[j]+0.5,ybins[i]+0.5, hist.T[i,j], 
                    color="w", ha="center", va="center", fontweight="bold")

## load and initialize container
cont = ts_digi_container('test.root','LDMX_Events')
cont.get_digi_collection('trigScintDigisTag_sim')
cont.get_digi_collection('trigScintDigisUp_sim')
cont.get_digi_collection('trigScintDigisDn_sim')

threshold=50

## get the true number of beam electrons for all events
electrons=cont.get_num_beam_electrons()

## get hits from tagger array for all events and predict num. electrons
tag_hits30=cont.count_hits('trigScintDigisTag_sim',threshold)
tag_hits30_pred=np.divide(np.add(tag_hits30,1),2)

## get hits from upstream array for all events and predict num. electrons
up_hits30=cont.count_hits('trigScintDigisUp_sim',threshold)
up_hits30_pred=np.divide(np.add(up_hits30,1),2)

## get hits from downstream array for all events and predict num. electrons
dn_hits30=cont.count_hits('trigScintDigisDn_sim',threshold)
dn_hits30_pred=np.divide(np.add(dn_hits30,1),2)

## make prediction based on the minimum value of the above three predictions
vote=map(lambda x,y,z:np.min([x,y,z]),up_hits30_pred,tag_hits30_pred,dn_hits30_pred)

## dump in formation for events in which prediction is over-estimating truth by 1
cont.dump(np.argwhere(np.subtract(vote,electrons)==1).flatten())

## plot
plot_conf_matrix(electrons,vote)
plt.show()
