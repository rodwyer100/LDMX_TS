import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from ts_digi_container import *
import ROOT as r

## initialize container
cont = ts_digi_container('test.root','LDMX_Events')
cont.get_digi_collection('trigScintDigisTag_sim')
cont.get_digi_collection('trigScintDigisUp_sim')
cont.get_digi_collection('trigScintDigisDn_sim')
