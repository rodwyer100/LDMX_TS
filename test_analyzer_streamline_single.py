from ts_digi_container import *
import ROOT as r

#import simulaton and histogram type
sim = raw_input("Simulation ROOT file: ")
hist_dim = raw_input("1D or 2D Histogram: ")

## initialize container
cont = ts_digi_container(sim,'LDMX_Events')
cont.get_digi_collection('trigScintDigisTag_sim')
cont.get_digi_collection('trigScintDigisUp_sim')
cont.get_digi_collection('trigScintDigisDn_sim')
modules = ['trigScintDigisTag_sim', 'trigScintDigisUp_sim', 'trigScintDigisDn_sim']

## configuration for pretty root plots
r.gROOT.ProcessLine(".L tdrstyle.C")
r.gROOT.ProcessLine("setTDRStyle()")

#acquire inputs for script configuration (RHE = Relative Hit Efficiency, EEP = Electron Escape Probability)
variable = raw_input('Parameter 1 : ')
x_ax = raw_input('X axis: ')
xbins = int(raw_input('X bins: '))
xlow = float(raw_input('X low: '))
xhigh = float(raw_input('X high: '))
veto = raw_input('Total Hits, Real Electron, or Pure Noise: ')
aper_tog = raw_input('Toggle EEP? ')
pNoise = raw_input('Exclude pure noise? ')
sNoise = raw_input('Exclude secondaries? ')
if (hist_dim == '2D'):
	variable2 = raw_input('Parameter 2: ')
	y_ax = raw_input('Y axis: ')
	ybins = int(raw_input('Y bins: '))
	ylow = float(raw_input('Y low: '))
	yhigh = float(raw_input('Y high: '))

## initialize root histogram
hist1 = r.TH1F("2e_tag_" + variable + "_100R_v2","Title;" + x_ax + ";Hits",xbins,xlow,xhigh)
hist2 = r.TH1F("2e_up_" + variable + "_100R_v2","Title;" + x_ax + ";Hits",xbins,xlow,xhigh)
hist3 = r.TH1F("2e_down_" + variable + "_100R_v2","Title;" + x_ax + ";Hits",xbins,xlow,xhigh)
hists = [hist1, hist2, hist3]
hist4 = r.TH2F("2e_tag_aper_prob_100R_v2","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hist5 = r.TH2F("2e_up_aper_prob_100R_v2","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hist6 = r.TH2F("2e_down_aper_prob_100R_v2","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hists_aper = [hist4, hist5, hist6]
if (hist_dim == '2D'):
	hist7 = r.TH2F("2e_tag_" + variable + "_" + variable2 + "_100R_v2","Title;" + x_ax + ";" + y_ax,xbins,xlow,xhigh,ybins,ylow,yhigh)
	hist8 = r.TH2F("2e_up_" + variable + "_" + variable2 + "_100R_v2","Title;" + x_ax + ";" + y_ax,xbins,xlow,xhigh,ybins,ylow,yhigh)
	hist9 = r.TH2F("2e_down_" + variable + "_" + variable2 + "_100R_v2","Title;" + x_ax + ";" + y_ax,xbins,xlow,xhigh,ybins,ylow,yhigh)
	hists = [hist7, hist8, hist9]

#record relative hit efficiency and secondary parameters
heven_r = [0,0,0]
hodd_r = [0,0,0]
heven_f = [0,0,0]
hodd_f = [0,0,0]
entries_r = [0,0,0] 	#scale factor is configured in simulation generation script when user determines number of e-/event
entries_f=[0,0,0]

#cumulative calculations of EEP per module
#hit_dict_tag = {}
#hit_dict_up = {}
#hit_dict_down ={}
#hit_dicts = [hit_dict_tag, hit_dict_up,hit_dict_down]
#for i in range(len(hit_dicts)):
#	for j in range(50):
#		hit_dicts[i][j] = 0


def aper_ratio(x, next_x, prev_x):
        return (float(next_x + prev_x)/x)


## loop over events
for i in range(cont.tree.numentries):
    for j in range(len(modules)) :
    	## get list of pe for tagger array for event i
    	params = cont.get_data(modules[j],variable,i)
	if (hist_dim == "2D"):
		params2 = cont.get_data(modules[j],variable2,i)
    	barNums=cont.get_data(modules[j],'barID',i)
    	noiseDiscr = cont.get_data(modules[j],'isNoise',i)
	rnoiseDiscr = cont.get_data(modules[j],'beamEfrac',i)
	hit_dict = {}
	for l in range(50):
		hit_dict[l] = 0
    	for k in range(len(params)) :  
		if ((hist_dim == '1D') and ((pNoise.lower() == 'n') or ((pNoise.lower() == 'y') and (noiseDiscr[k] == False))) and ((sNoise.lower() == 'n') or ((sNoise.lower() == 'y') and ((rnoiseDiscr[k] < 0.2) or (rnoiseDiscr[k] > 0.9)) ))):
        		hists[j].Fill(params[k])
		if ((hist_dim == '2D') and ((pNoise.lower() == 'n') or ((pNoise.lower() == 'y') and (noiseDiscr[k] == False))) and ((sNoise.lower() == 'n') or ((sNoise.lower() == 'y') and ((rnoiseDiscr[k] < 0.2) or (rnoiseDiscr[k] > 0.9)) ))):
			hists[j].Fill(params[k],params2[k])
		hit_dict[barNums[k]]+=1
		if (rnoiseDiscr[k] > 0.9):
			entries_r[j]+=1
			if (barNums[k] % 2 == 0):
                		heven_r[j]+=1
        		else:
                		hodd_r[j]+=1
		if (rnoiseDiscr[k] <= 0.9):
			entries_f[j]+=1	
        		if (barNums[k] % 2 == 0):
				heven_f[j]+=1
			else:
				hodd_f[j]+=1
	if(aper_tog.lower() == 'y'):
		bars = hit_dict.keys()
		hits = hit_dict.values()
		for n in range(1,len(bars)-1):
			if ((n % 2 != 0) and (hits[n] != 0)):
				hists_aper[j].Fill(bars[n],aper_ratio(hits[n],hits[n+1],hits[n-1]))
		if (hits[len(hits)-1] != 0):
			hists_aper[j].Fill(bars[len(hits)-1],(hits[len(hits)-2]/hits[len(hits)-1]))                                                                                                                                                                                     



#plot!
c1 = r.TCanvas("c1", "hist1 canvas", 600,  500)
hists[0].SetFillColor(2)
hists[0].SetLineColor(4)
hists[0].SetLineStyle(2)
if (hist_dim == '1D'):
	hists[0].Draw()
if (hist_dim == '2D'):
	hists[0].Draw("COLZ")
c1.SetRightMargin( 5.*c1.GetRightMargin() )
if (hist_dim == '1D'):
	leg1 = r.TLegend(0.8,0.7,1.0,0.9)
if (hist_dim == '2D'):
	leg1 = r.TLegend(0.6,0.7,0.8,0.9)
if (veto == 'Total Hits'):
        leg1.SetHeader("Total Hits = " + str(entries_r[0] + entries_f[0]), "C")
if (veto == 'Real Electron'):
        leg1.SetHeader("Electron Hits = " + str(entries_r[0]), "C")
if (veto == 'Pure Noise'):
        leg1.SetHeader("Noise Hits = " + str(entries_f[0]), "C")
leg1.Draw()


c2 = r.TCanvas("c2", "hist2 canvas", 600,  500)
hists[1].SetFillColor(2)
hists[1].SetLineColor(4)
hists[1].SetLineStyle(2)
if (hist_dim == '1D'):
        hists[1].Draw()
if (hist_dim == '2D'):
        hists[1].Draw("COLZ")
c2.SetRightMargin( 5.*c2.GetRightMargin() )
if (hist_dim == '1D'):
        leg2 = r.TLegend(0.8,0.7,1.0,0.9)
if (hist_dim == '2D'):
        leg2 = r.TLegend(0.6,0.7,0.8,0.9)
if (veto == 'Total Hits'):
        leg2.SetHeader("Total Hits = " + str(entries_r[1] + entries_f[1]), "C")
if (veto == 'Real Electron'):
        leg2.SetHeader("Electron Hits = " + str(entries_r[1]), "C")
if (veto == 'Pure Noise'):
        leg2.SetHeader("Noise Hits = " + str(entries_f[1]), "C")
leg2.Draw()

c3 = r.TCanvas("c3", "hist3 canvas", 600,  500)
hists[2].SetFillColor(2)
hists[2].SetLineColor(4)
hists[2].SetLineStyle(2)
if (hist_dim == '1D'):
        hists[2].Draw()
if (hist_dim == '2D'):
        hists[2].Draw("COLZ")
c3.SetRightMargin( 5.*c3.GetRightMargin() )
if (hist_dim == '1D'):
        leg3 = r.TLegend(0.8,0.7,1.0,0.9)
if (hist_dim == '2D'):
        leg3 = r.TLegend(0.6,0.7,0.8,0.9)
if (veto == 'Total Hits'):
	leg3.SetHeader("Total Hits = " + str(entries_r[2] + entries_f[2]), "C")
if (veto == 'Real Electron'):
	leg3.SetHeader("Electron Hits = " + str(entries_r[2]), "C")
if (veto == 'Pure Noise'):
	leg3.SetHeader("Noise Hits = " + str(entries_f[2]), "C")
leg3.Draw()


#generate histograms for electron escape probability
if (aper_tog.lower() == 'y'):
	#for i in range(len(hists_aper)):
	#	bars = hit_dicts[i].keys()
	#	hits = hit_dicts[i].values()
	#	#hists_aper[i].Fill(bars[0],(hits[1]/hits[0]))
	#	for j in range(1,len(bars)-1):
	#		if (j % 2 != 0):
	#			hists_aper[i].Fill(bars[j],aper_ratio(hits[j],hits[j+1],hits[j-1]))
	#	hists_aper[i].Fill(bars[len(hits)-1],(hits[len(hits)-2]/hits[len(hits)-1]))


	c4 = r.TCanvas("c4", "hist4 canvas", 600,  500)
	hists_aper[0].SetFillColor(2)
	hists_aper[0].SetLineColor(4)
	hists_aper[0].SetLineStyle(2)
	c4.SetRightMargin( 5.*c4.GetRightMargin() )
	hists_aper[0].Draw("COLZ")

	c5 = r.TCanvas("c5", "hist5 canvas", 600,  500)
        hists_aper[1].SetFillColor(2)
        hists_aper[1].SetLineColor(4)
        hists_aper[1].SetLineStyle(2)
        c5.SetRightMargin( 5.*c5.GetRightMargin() )
	hists_aper[1].Draw("COLZ")

	c6 = r.TCanvas("c6", "hist6 canvas", 600,  500)
        hists_aper[2].SetFillColor(2)
        hists_aper[2].SetLineColor(4)
        hists_aper[2].SetLineStyle(2)
        c6.SetRightMargin( 5.*c6.GetRightMargin() )
	hists_aper[2].Draw("COLZ")

#archive histograms
c1.SaveAs( hists[0].GetName()+".png")
c2.SaveAs( hists[1].GetName()+".png")
c3.SaveAs( hists[2].GetName()+".png")
if (aper_tog.lower() == 'y'):
	c4.SaveAs( hists_aper[0].GetName()+".png")
	c5.SaveAs( hists_aper[1].GetName()+".png")
	c6.SaveAs( hists_aper[2].GetName()+".png")

#readout true, real, and noise RHE's
print('tRHE = [' + str(float((heven_r[0] + heven_f[0]))/(hodd_r[0] + hodd_f[0])) + ',' + str(float((heven_r[1] + heven_f[1]))/(hodd_r[1] + hodd_f[1]))+ ',' + str(float((heven_r[2] + heven_f[2]))/(hodd_r[2] + hodd_f[2])) + ']')
print('rRHE = [' + str(float(heven_r[0])/hodd_r[0]) + ',' + str(float(heven_r[1])/hodd_r[1]) + ',' + str(float(heven_r[2])/hodd_r[2]) + ']')
print('fRHE = [' + str(float(heven_f[0])/hodd_f[0]) + ',' + str(float(heven_f[1])/hodd_f[1]) + ',' + str(float(heven_f[2])/hodd_f[2]) + ']')
