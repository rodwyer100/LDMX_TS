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
two_layer_prob = raw_input('Toggle Two Layer Probability? ')
pNoise = raw_input('Exclude pure noise? ')
sNoise = raw_input('Exclude secondaries? ')
if (hist_dim == '2D'):
	variable2 = raw_input('Parameter 2: ')
	y_ax = raw_input('Y axis: ')
	ybins = int(raw_input('Y bins: '))
	ylow = float(raw_input('Y low: '))
	yhigh = float(raw_input('Y high: '))

## initialize root histogram
hist1 = r.TH1F("1e_tag_" + variable + "_100R_allCuts","Title;" + x_ax + ";Hits",xbins,xlow,xhigh)
hist2 = r.TH1F("1e_up_" + variable + "_100R_allCuts","Title;" + x_ax + ";Hits",xbins,xlow,xhigh)
hist3 = r.TH1F("1e_down_" + variable + "_100R_allCuts","Title;" + x_ax + ";Hits",xbins,xlow,xhigh)
hists = [hist1, hist2, hist3]
hist4 = r.TH2F("1e_tag_aper_prob_100R_2D","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hist5 = r.TH2F("1e_up_aper_prob_100R_2D","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hist6 = r.TH2F("1e_down_aper_prob_100R_2D","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hists_aper = [hist4, hist5, hist6]
if (hist_dim == '2D'):
	hist7 = r.TH2F("1e_tag_" + variable + "_" + variable2 + "_100R_v2","Title;" + x_ax + ";" + y_ax,xbins,xlow,xhigh,ybins,ylow,yhigh)
	hist8 = r.TH2F("1e_up_" + variable + "_" + variable2 + "_100R_v2","Title;" + x_ax + ";" + y_ax,xbins,xlow,xhigh,ybins,ylow,yhigh)
	hist9 = r.TH2F("1e_down_" + variable + "_" + variable2 + "_100R_v2","Title;" + x_ax + ";" + y_ax,xbins,xlow,xhigh,ybins,ylow,yhigh)
	hists = [hist7, hist8, hist9]
#hist10 = r.TH1F("1e_tag_proj_barID","Title;barID;Hits",50,0,50)
#hist11 = r.TH1F("1e_up_proj_barID","Title;barID;Hits",50,0,50)
#hist12 = r.TH1F("1e_down_proj_barID","Title;barID;Hits",50,0,50)
#hists_projx = [hist10, hist11, hist12]
#hist13 = r.TH1F("1e_tag_proj_eep","Title;EEP;Hits",3,0,3)
#hist14 = r.TH1F("1e_up_proj_eep","Title;EEP;Hits",3,0,3)
#hist15 = r.TH1F("1e_down_proj_eep","Title;EEP;Hits",3,0,3)
#hists_projy = [hist13, hist14, hist15]
hist16 = r.TH1F("1e_tag_aper_odds_100R_allNoiseCuts","Title;barID;Hits",50,0,50)
hist17 = r.TH1F("1e_up_aper_odds_100R_allNoiseCuts","Title;barID;Hits",50,0,50)
hist18 = r.TH1F("1e_down_aper_odds_100R_allNoiseCuts","Title;barID;Hits",50,0,50)
hists_odds = [hist16, hist17,hist18]
hist19 = r.TH1F("1e_tag_aper_prob_100R_1D","Title;barID;G(Y)",50,0,50)
hist20 = r.TH1F("1e_up_aper_prob_100R_1D","Title;barID;G(Y)",50,0,50)
hist21 = r.TH1F("1e_down_aper_prob_100R_1D","Title;barID;G(Y)",50,0,50)
hists_odds_adj = [hist19, hist20, hist21]
hist22 = r.TH1F("1e_tag_two_layer_prob_100R_allNoiseCuts","Title;barID;Hits",50,0,50)
hist23 = r.TH1F("1e_up_two_layer_prob_100R_allNoiseCuts","Title;barID;Hits",50,0,50)
hist24 = r.TH1F("1e_down_two_layer_prob_100R_allNoiseCuts","Title;barID;Hits",50,0,50)
hists_evens = [hist22, hist23, hist24]
hist25 = r.TH1F("1e_tag_two_layer_prob_100R_1D","Title;barID;G(Y)",50,0,50)
hist26 = r.TH1F("1e_up_two_layer_prob_100R_1D","Title;barID;G(Y)",50,0,50)
hist27 = r.TH1F("1e_down_two_layer_prob_100R_1D","Title;barID;G(Y)",50,0,50)
hists_evens_adj = [hist25, hist26, hist27]
hist28 = r.TH2F("1e_tag_two_layer_prob_100R_2D","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hist29 = r.TH2F("1e_up_two_layer_prob_100R_2D","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hist30 = r.TH2F("1e_down_two_layer_prob_100R_2D","Title;Y (barID);F(Y)",50,0,50,50,0,5)
hists_two_layer = [hist28, hist29, hist30]

#record relative hit efficiency and secondary parameters
heven_r = [0,0,0]
hodd_r = [0,0,0]
heven_f = [0,0,0]
hodd_f = [0,0,0]
entries_r = [0,0,0] 	#scale factor is configured in simulation generation script when user determines number of e-/event
entries_f=[0,0,0]
spltsOdd = 0
totlOdd = 0
spltsEven = 0
totlEven = 0

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
yprev = 0

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
		if ((hist_dim == '1D') and ((pNoise.lower() == 'n') or ((pNoise.lower() == 'y') and (rnoiseDiscr[k] > 0.2))) and ((sNoise.lower() == 'n') or ((sNoise.lower() == 'y') and ((rnoiseDiscr[k] < 0.2) or (rnoiseDiscr[k] > 0.9)) ))):
			if (barNums[k] % 2 == 0):
				yLocal = params[k] - 3*(float(barNums[k] - 24)/2) - 0.3*((barNums[k] - 24)/2)
			if (barNums[k] % 2 != 0):
				yLocal = params[k] - 3*(float(barNums[k] - 25)/2) - 0.3*((barNums[k] - 25)/2)
			hists[j].Fill(yLocal)
			if (barNums[k] < 50):
                        	hit_dict[barNums[k]] = 1
		if ((hist_dim == '2D') and ((pNoise.lower() == 'n') or ((pNoise.lower() == 'y') and (rnoiseDiscr[k] >  0.2))) and ((sNoise.lower() == 'n') or ((sNoise.lower() == 'y') and ((rnoiseDiscr[k] < 0.2) or (rnoiseDiscr[k] > 0.9)) ))):
			hists[j].Fill(params[k],params2[k])
			if (barNums[k] < 50):
                        	hit_dict[barNums[k]] = 1
		#if (rnoiseDiscr[k] > 0.9):
			#entries_r[j]+=1
			#if (barNums[k] % 2 == 0):
                		#heven_r[j]+=1
        		#else:
                		#hodd_r[j]+=1
		#if (rnoiseDiscr[k] <= 0.9):
			#entries_f[j]+=1	
        		#if (barNums[k] % 2 == 0):
				#heven_f[j]+=1
			#else:
				#hodd_f[j]+=1
	if(aper_tog.lower() == 'y'):
		bars = hit_dict.keys()
		hits = hit_dict.values()
		for n in range(1,len(bars)-1):
			if ((n % 2 != 0) and (hits[n] != 0)):
				#encoding for 2D EEP Histograms
				hists_aper[j].Fill(bars[n],aper_ratio(hits[n],hits[n+1],hits[n-1]))
				#encoding for 1D EEP histograms
				hists_odds[j].Fill(n)
				if ((hits[n-1] != 0) or (hits[n+1] != 0)):
					hists_odds_adj[j].Fill(n)
				#hists_projx[j].Fill(bars[n])
				#hists_projy[j].Fill(aper_ratio(hits[n],hits[n+1],hits[n-1]))
				totlOdd+=1
				if (aper_ratio(hits[n],hits[n+1],hits[n-1]) == 0):
					spltsOdd+=1
		if (hits[len(hits)-1] != 0):
			hists_aper[j].Fill(bars[len(hits)-1],(hits[len(hits)-2]/hits[len(hits)-1]))
			hists_odds[j].Fill(len(hits)-1)
			if (hits[len(hits)-2] != 0):
				hists_odds_adj[j].Fill(len(hits)-1)  
	if(two_layer_prob.lower() == 'y'):
                bars = hit_dict.keys()
                hits = hit_dict.values()
                for n in range(2,len(bars)-1):
                        if ((n % 2 == 0) and (hits[n] != 0)):
                                hists_two_layer[j].Fill(bars[n],aper_ratio(hits[n],hits[n+1],hits[n-1]))
                                hists_evens[j].Fill(n)
                                if ((hits[n-1] != 0) or (hits[n+1] != 0)):
                                        hists_evens_adj[j].Fill(n)
                                #hists_projx[j].Fill(bars[n])
                                #hists_projy[j].Fill(aper_ratio(hits[n],hits[n+1],hits[n-1]))
                                totlEven+=1
                                if (aper_ratio(hits[n],hits[n+1],hits[n-1]) == 0):
                                        spltsEven+=1
                if (hits[0] != 0):
                        hists_two_layer[j].Fill(bars[0],(hits[1]/hits[0]))
                        hists_evens[j].Fill(0)
                        if (hits[1] != 0):
                                hists_evens_adj[j].Fill(0)


	

                                                                                                                                                                                   
	for m in range(len(rnoiseDiscr)):
		if (rnoiseDiscr[m] > 0.9):
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

print(yprev)
#plot!
c1 = r.TCanvas("c1", "hist1 canvas", 600,  500)
#hists[0].SetFillColorAlpha(2,0.3)
hists[0].SetLineColor(2)
hists[0].SetLineStyle(1)
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
        leg1.SetHeader("Total Hits = " + str(entries_r[0] + entries_f[0]+ entries_r[1] + entries_f[1] + entries_r[2] + entries_f[2]), "C")
if (veto == 'Real Electron'):
        leg1.SetHeader("Electron Hits = " + str(entries_r[0] + entries_r[1] + entries_r[2]), "C")
if (veto == 'Pure Noise'):
        leg1.SetHeader("Noise Hits = " + str(entries_f[0] + entries_f[1] + entries_f[2]), "C")
leg1.AddEntry(hists[0],"Tagger","L")
leg1.Draw()


#c2 = r.TCanvas("c2", "hist2 canvas", 600,  500)
#hists[1].SetFillColorAlpha(3,0.3)
hists[1].SetLineColor(3)
hists[1].SetLineStyle(1)
if (hist_dim == '1D'):
        hists[1].Draw("same")
if (hist_dim == '2D'):
        hists[1].Draw("sameCOLZ")
#c2.SetRightMargin( 5.*c2.GetRightMargin() )
#if (hist_dim == '1D'):
 #       leg2 = r.TLegend(0.8,0.7,1.0,0.9)
#if (hist_dim == '2D'):
 #       leg2 = r.TLegend(0.6,0.7,0.8,0.9)
#if (veto == 'Total Hits'):
 #       leg2.SetHeader("Total Hits = " + str(entries_r[1] + entries_f[1]), "C")
#if (veto == 'Real Electron'):
 #       leg2.SetHeader("Electron Hits = " + str(entries_r[1]), "C")
#if (veto == 'Pure Noise'):
 #       leg2.SetHeader("Noise Hits = " + str(entries_f[1]), "C")
#leg2.Draw()
leg1.AddEntry(hists[1],"Upstream","L")

#c3 = r.TCanvas("c3", "hist3 canvas", 600,  500)
#hists[2].SetFillColorAlpha(4,0.3)
hists[2].SetLineColor(5)
hists[2].SetLineStyle(1)
if (hist_dim == '1D'):
        hists[2].Draw("same")
if (hist_dim == '2D'):
        hists[2].Draw("sameCOLZ")
#c3.SetRightMargin( 5.*c3.GetRightMargin() )
#if (hist_dim == '1D'):
 #       leg3 = r.TLegend(0.8,0.7,1.0,0.9)
#if (hist_dim == '2D'):
 #       leg3 = r.TLegend(0.6,0.7,0.8,0.9)
#if (veto == 'Total Hits'):
#	leg3.SetHeader("Total Hits = " + str(entries_r[2] + entries_f[2]), "C")
#if (veto == 'Real Electron'):
#	leg3.SetHeader("Electron Hits = " + str(entries_r[2]), "C")
#if (veto == 'Pure Noise'):
#	leg3.SetHeader("Noise Hits = " + str(entries_f[2]), "C")
#leg3.Draw()
leg1.AddEntry(hists[2],"Downstream","L")


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

#c7 = r.TCanvas("c7", "hist7 canvas", 600,  500)
#hists_projx[0].SetFillColor(2)
#hists_projx[0].SetLineColor(4)
#hists_projx[0].SetLineStyle(2)
#c7.SetRightMargin( 5.*c7.GetRightMargin() )
#hists_projx[0].Draw()

#c8 = r.TCanvas("c8", "hist8 canvas", 600,  500)
#hists_projx[1].SetFillColor(2)
#hists_projx[1].SetLineColor(4)
#hists_projx[1].SetLineStyle(2)
#c8.SetRightMargin( 5.*c8.GetRightMargin() )
#hists_projx[1].Draw()

#c9 = r.TCanvas("c9", "hist9 canvas", 600,  500)
#hists_projx[2].SetFillColor(2)
#hists_projx[2].SetLineColor(4)
#hists_projx[2].SetLineStyle(2)
#c9.SetRightMargin( 5.*c9.GetRightMargin() )
#hists_projx[2].Draw()

#c10 = r.TCanvas("c10", "hist10 canvas", 600,  500)
#hists_projy[0].SetFillColor(2)
#hists_projy[0].SetLineColor(4)
#hists_projy[0].SetLineStyle(2)
#c10.SetRightMargin( 5.*c10.GetRightMargin() )
#hists_projy[0].Draw()

#c11 = r.TCanvas("c11", "hist11 canvas", 600,  500)
#hists_projy[1].SetFillColor(2)
#hists_projy[1].SetLineColor(4)
#hists_projy[1].SetLineStyle(2)
#c11.SetRightMargin( 5.*c11.GetRightMargin() )
#hists_projy[1].Draw()

#c12 = r.TCanvas("c12", "hist12 canvas", 600,  500)
#hists_projy[2].SetFillColor(2)
#hists_projy[2].SetLineColor(4)
#hists_projy[2].SetLineStyle(2)
#c12.SetRightMargin( 5.*c12.GetRightMargin() )
#hists_projy[2].Draw()


	c13 = r.TCanvas("c13", "hist16 canvas", 600,  500)
	#hists_odds[0].SetFillColor(3)
	hists_odds[0].SetLineColor(5)
	hists_odds[0].SetLineStyle(2)
	#hists_odds_adj[0].SetFillColor(2)
	hists_odds_adj[0].SetLineColor(2)
	hists_odds_adj[0].SetLineStyle(1)
	print(hists_odds_adj[0].GetBinContent(2))
	print(hists_odds[0].GetBinContent(2))
	hists_odds_adj[0].Divide(hists_odds_adj[0],hists_odds[0],1,1,"B")
	print(hists_odds_adj[0].GetBinContent(2))
	print(hists_odds_adj[0].GetBinError(2))
	c13.SetRightMargin( 5.*c13.GetRightMargin() )
	leg4 = r.TLegend(0.8,0.7,1.0,0.9)
	leg4.AddEntry(hists_odds_adj[0],"Tagger","L")
	hists_odds_adj[0].Draw("he")

	#c14 = r.TCanvas("c14", "hist17 canvas", 600,  500)
	#hists_odds[1].SetFillColor(3)
	hists_odds[1].SetLineColor(5)
	hists_odds[1].SetLineStyle(2)
	#hists_odds_adj[1].SetFillColor(4)
	hists_odds_adj[1].SetLineColor(3)
	hists_odds_adj[1].SetLineStyle(1)
	hists_odds_adj[1].Divide(hists_odds_adj[1],hists_odds[1],1,1,"B")
	print(hists_odds_adj[1].GetBinError(2))
	#c14.SetRightMargin( 5.*c14.GetRightMargin() )
	leg4.AddEntry(hists_odds_adj[1],"Upstream","L")
	hists_odds_adj[1].Draw("hesame")

	#c15 = r.TCanvas("c15", "hist18 canvas", 600,  500)
	#hists_odds[2].SetFillColor(3)
	hists_odds[2].SetLineColor(5)
	hists_odds[2].SetLineStyle(2)
	#hists_odds_adj[2].SetFillColor(5)
	hists_odds_adj[2].SetLineColor(1)
	hists_odds_adj[2].SetLineStyle(1)
	hists_odds_adj[2].Divide(hists_odds_adj[2],hists_odds[2],1,1,"B")
	print(hists_odds_adj[2].GetBinError(2))
	#c15.SetRightMargin( 5.*c15.GetRightMargin() )
	leg4.AddEntry(hists_odds_adj[2],"Downstream","L")
	leg4.Draw()
	hists_odds_adj[2].Draw("hesame")

if (two_layer_prob.lower() == 'y'):
	c16 = r.TCanvas("c16", "hist19 canvas", 600,  500)
	#hists_evens[0].SetFillColor(3)
	hists_evens[0].SetLineColor(5)
	hists_evens[0].SetLineStyle(2)
	#hists_evens_adj[0].SetFillColor(2)
	hists_evens_adj[0].SetLineColor(2)
	hists_evens_adj[0].SetLineStyle(1)
	hists_evens_adj[0].Divide(hists_evens_adj[0],hists_evens[0],1,1,"B")
	print(hists_evens_adj[0].GetBinError(1))
	c16.SetRightMargin( 5.*c16.GetRightMargin() )
	leg5 = r.TLegend(0.8,0.7,1.0,0.9)
	leg5.AddEntry(hists_evens_adj[0],"Tagger","L")
	hists_evens_adj[0].Draw("he")

	#c17 = r.TCanvas("c17", "hist20 canvas", 600,  500)
	#hists_evens[1].SetFillColor(3)
	hists_evens[1].SetLineColor(5)
	hists_evens[1].SetLineStyle(2)
	#hists_evens_adj[1].SetFillColor(4)
	hists_evens_adj[1].SetLineColor(3)
	hists_evens_adj[1].SetLineStyle(1)
	hists_evens_adj[1].Divide(hists_evens_adj[1],hists_evens[1],1,1,"B")
	print(hists_evens_adj[1].GetBinError(1))
	#c17.SetRightMargin( 5.*c17.GetRightMargin() )
	leg5.AddEntry(hists_evens_adj[1],"Upstream","L")
	hists_evens_adj[1].Draw("hesame")

	#c18 = r.TCanvas("c18", "hist21 canvas", 600,  500)
	#hists_evens[2].SetFillColor(3)
	hists_evens[2].SetLineColor(5)
	hists_evens[2].SetLineStyle(2)
	#hists_evens_adj[2].SetFillColor(5)
	hists_evens_adj[2].SetLineColor(1)
	hists_evens_adj[2].SetLineStyle(1)
	hists_evens_adj[2].Divide(hists_evens_adj[2],hists_evens[2],1,1,"B")
	print(hists_evens_adj[2].GetBinError(1))
	#c18.SetRightMargin( 5.*c18.GetRightMargin() )
	leg5.AddEntry(hists_evens_adj[2],"Downstream","L")
	leg5.Draw()
	hists_evens_adj[2].Draw("hesame")

	c19 = r.TCanvas("c19", "hist28 canvas", 600,  500)
        hists_two_layer[0].SetFillColor(2)
        hists_two_layer[0].SetLineColor(4)
        hists_two_layer[0].SetLineStyle(2)
        c19.SetRightMargin( 5.*c19.GetRightMargin() )
        hists_two_layer[0].Draw("COLZ")

        c20 = r.TCanvas("c20", "hist29 canvas", 600,  500)
        hists_two_layer[1].SetFillColor(2)
        hists_two_layer[1].SetLineColor(4)
        hists_two_layer[1].SetLineStyle(2)
        c20.SetRightMargin( 5.*c20.GetRightMargin() )
        hists_two_layer[1].Draw()

        c21 = r.TCanvas("c21", "hist30 canvas", 600,  500)
        hists_two_layer[2].SetFillColor(2)
        hists_two_layer[2].SetLineColor(4)
        hists_two_layer[2].SetLineStyle(2)
        c21.SetRightMargin( 5.*c21.GetRightMargin() )
        hists_two_layer[2].Draw()





#archive histograms
c1.SaveAs( hists[0].GetName()+".png")
#c2.SaveAs( hists[1].GetName()+".png")
#c3.SaveAs( hists[2].GetName()+".png")
if (aper_tog.lower() == 'y'):
	c4.SaveAs( hists_aper[0].GetName()+".png")
	c5.SaveAs( hists_aper[1].GetName()+".png")
	c6.SaveAs( hists_aper[2].GetName()+".png")
#c7.SaveAs( hists_projx[0].GetName()+".png")
#c8.SaveAs( hists_projx[1].GetName()+".png")
#c9.SaveAs( hists_projx[2].GetName()+".png")
#c10.SaveAs( hists_projy[0].GetName()+".png")
#c11.SaveAs( hists_projy[1].GetName()+".png")
#c12.SaveAs( hists_projy[2].GetName()+".png")
	c13.SaveAs( hists_odds_adj[0].GetName()+".png")
	#c14.SaveAs( hists_odds_adj[1].GetName()+".png")
	#c15.SaveAs( hists_odds_adj[2].GetName()+".png")
if (two_layer_prob.lower() == 'y'):
	c16.SaveAs( hists_evens_adj[0].GetName()+".png")
	#c17.SaveAs( hists_evens_adj[1].GetName()+".png")
	#c18.SaveAs( hists_evens_adj[2].GetName()+".png")
	c19.SaveAs( hists_two_layer[0].GetName()+".png")
	c20.SaveAs( hists_two_layer[1].GetName()+".png")
	c21.SaveAs( hists_two_layer[2].GetName()+".png")

#readout total, real, and noise RHE's
print('tRHE = [' + str(float((heven_r[0] + heven_f[0]))/(hodd_r[0] + hodd_f[0])) + ',' + str(float((heven_r[1] + heven_f[1]))/(hodd_r[1] + hodd_f[1]))+ ',' + str(float((heven_r[2] + heven_f[2]))/(hodd_r[2] + hodd_f[2])) + ']')
print('rRHE = [' + str(float(heven_r[0])/hodd_r[0]) + ',' + str(float(heven_r[1])/hodd_r[1]) + ',' + str(float(heven_r[2])/hodd_r[2]) + ']')
print('fRHE = [' + str(float(heven_f[0])/hodd_f[0]) + ',' + str(float(heven_f[1])/hodd_f[1]) + ',' + str(float(heven_f[2])/hodd_f[2]) + ']')
if (totlOdd != 0):
	print('EEP Split Prob:' + str((float(spltsOdd)/totlOdd)*100))
if (totlEven != 0):
	print('Two Layer Prob:' + str((float(spltsEven)/totlEven)*100))
