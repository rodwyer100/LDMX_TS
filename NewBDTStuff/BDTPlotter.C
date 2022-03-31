#include <stdio.h>
#include "TFile.h"
#include "TTree.h"
#include "TTreeReader.h"
#include "TTreeReaderArray.h"
#include "TH1F.h"
#include "TCanvas.h"
#include <fstream>
#include <iostream>
#include <iomanip>

void BDTPlotter(){


TFile *myFile=TFile::Open("ClusterResidualRunNewW8.root");//"autorunout33.root");
myFile->cd("/dataset/Method_BDT/BDT");
gDirectory->ls();
//myFile->Map();
//myFile->cd("dataset/Method_BDT");
//myFile->pwd()
//auto hs = new THStack("hs","BDT Response Curves");
//TH1D *h1=(TH1D*)gDirectory->Get("clPEDn1__Signal");	
//TH1D *h2=(TH1D*)gDirectory->Get("clPEDn1__Background");	

//TH1D *h1=(TH1D*)gDirectory->Get("hitTimeDn__Signal");	
//TH1D *h2=(TH1D*)gDirectory->Get("hitTimeDn__Background");

TH1D *h7=(TH1D*)gDirectory->Get("clPEDn1__Signal");	
TH1D *h8=(TH1D*)gDirectory->Get("clPEDn1__Background");

TH1D *h9=(TH1D*)gDirectory->Get("clPEUp1__Signal");	
TH1D *h10=(TH1D*)gDirectory->Get("clPEUp1__Background");

TH1D *h11=(TH1D*)gDirectory->Get("clPETag1__Signal");	
TH1D *h12=(TH1D*)gDirectory->Get("clPETag1__Background");

TH1D *h1=(TH1D*)gDirectory->Get("clTimeDn__Signal");	
TH1D *h2=(TH1D*)gDirectory->Get("clTimeDn__Background");

TH1D *h3=(TH1D*)gDirectory->Get("clTimeUp__Signal");	
TH1D *h4=(TH1D*)gDirectory->Get("clTimeUp__Background");

TH1D *h5=(TH1D*)gDirectory->Get("clTimeTag__Signal");	
TH1D *h6=(TH1D*)gDirectory->Get("clTimeTag__Background");

TH1D *h13=(TH1D*)gDirectory->Get("residual__Signal");	
TH1D *h14=(TH1D*)gDirectory->Get("residual__Background");

TH1D *h15=(TH1D*)gDirectory->Get("clusterAv__Signal");	
TH1D *h16=(TH1D*)gDirectory->Get("clusterAv__Background");

TH1D *h17=(TH1D*)gDirectory->Get("clusterRes__Signal");	
TH1D *h18=(TH1D*)gDirectory->Get("clusterRes__Background");

TH1D *h19=(TH1D*)gDirectory->Get("MVA_BDT_S");	
TH1D *h20=(TH1D*)gDirectory->Get("MVA_BDT_B");

TH1D *h21=(TH1D*)gDirectory->Get("MVA_BDT_effBvsS");


//h1->SetTitle("Good Track Dn PE");
//h2->SetTitle("Bad Track Dn PE");
h1->SetTitle("Good Track Down Time");
h2->SetTitle("Bad Track Down Time");

h3->SetTitle("Good Track Up Time");
h4->SetTitle("Bad Track Up Time");

h5->SetTitle("Good Track Tag Time");
h6->SetTitle("Bad Track Tag Time");

h7->SetTitle("Good Track Dn PE Count");
h8->SetTitle("Bad Track Dn PE Count");

h9->SetTitle("Good Track UP PE Count");
h10->SetTitle("Bad Track UP PE Count");

h11->SetTitle("Good Track Tag PE Count");
h12->SetTitle("Bad Track Tag PE Count");

h13->SetTitle("Good Track Residual (bar)");
h14->SetTitle("Bad Track Residual (bar)");

h15->SetTitle("Good Track Cluster Average (PE)");
h16->SetTitle("Bad Track Cluster Average (PE)");

h17->SetTitle("Good Track Cluster Res (PE)");
h18->SetTitle("Bad Track Cluster Res (PE)");

h19->SetTitle("Signal Response Curve");
h20->SetTitle("Background Response Curve");

h21->SetTitle("Efficiency Curve (ROC)");

TCanvas c1;

c1.cd(1);
h1->GetXaxis()->SetTitle("Down Time (ns)");
h1->GetYaxis()->SetTitle("Normalized Track No.");	
h1->Draw("bar");
h1->Scale(1./h1->Integral());
h1->SetFillColorAlpha(kGreen,.35);
h2->SetFillColorAlpha(kRed,.4);
h2->Scale(1./h2->Integral());
h2->Draw("bar same");
TLegend *leg1 = c1.BuildLegend(.75,.75,1,1);
c1.SaveAs("DownTime.png");

TCanvas c2;

c2.cd(1);
h3->GetXaxis()->SetTitle("Up Time (ns)");
h3->GetYaxis()->SetTitle("Normalized Track No.");
h3->Draw("bar");
h3->Scale(1./h3->Integral());
h3->SetFillColorAlpha(kGreen,.35);
h4->SetFillColorAlpha(kRed,.4);
h4->Scale(1./h4->Integral());
h4->Draw("bar same");
TLegend *leg2 = c2.BuildLegend(.75,.75,1,1);
c2.SaveAs("UpTime.png");

TCanvas c3;

c3.cd(1);
h5->GetXaxis()->SetTitle("Tag Time (ns)");
h5->GetYaxis()->SetTitle("Normalized Track No.");
h5->Draw("bar");
h5->Scale(1./h5->Integral());
h5->SetFillColorAlpha(kGreen,.35);
h6->SetFillColorAlpha(kRed,.4);
h6->Scale(1./h6->Integral());
h6->Draw("bar same");
TLegend *leg3 = c3.BuildLegend(.75,.75,1,1);
c3.SaveAs("TagTime.png");


TCanvas c4;

c4.cd(1);
h7->GetXaxis()->SetTitle("Down PE Count");
h7->GetYaxis()->SetTitle("Normalized Track No.");
h7->Draw("bar");
h7->Scale(1./h7->Integral());
h7->SetFillColorAlpha(kGreen,.35);
h8->SetFillColorAlpha(kRed,.4);
h8->Scale(1./h8->Integral());
h8->Draw("bar same");
TLegend *leg4 = c4.BuildLegend(.75,.75,1,1);
c4.SaveAs("DownPE.png");

TCanvas c5;

c5.cd(1);
h9->GetXaxis()->SetTitle("Up PE Count");
h9->GetYaxis()->SetTitle("Normalized Track No.");
h9->Draw("bar");
h9->Scale(1./h9->Integral());
h9->SetFillColorAlpha(kGreen,.35);
h10->SetFillColorAlpha(kRed,.4);
h10->Scale(1./h10->Integral());
h10->Draw("bar same");
TLegend *leg5 = c5.BuildLegend(.75,.75,1,1);
c5.SaveAs("UpPE.png");

TCanvas c6;

c6.cd(1);
h11->GetXaxis()->SetTitle("Tag PE Count");
h11->GetYaxis()->SetTitle("Normalized Track No.");
h11->Draw("bar");
h11->Scale(1./h11->Integral());
h11->SetFillColorAlpha(kGreen,.35);
h12->SetFillColorAlpha(kRed,.4);
h12->Scale(1./h12->Integral());
h12->Draw("bar same");
TLegend *leg6 = c6.BuildLegend(.75,.75,1,1);
c6.SaveAs("TagPE.png");


TCanvas c7;

c7.cd(1);
h13->GetXaxis()->SetTitle("Residual (bar)");
h13->GetYaxis()->SetTitle("Normalized Track No.");
h13->Draw("bar");
h13->Scale(1./h13->Integral());
h13->SetFillColorAlpha(kGreen,.35);
h14->SetFillColorAlpha(kRed,.4);
h14->Scale(1./h14->Integral());
h14->Draw("bar same");
TLegend *leg7 = c7.BuildLegend(.75,.75,1,1);
c7.SaveAs("residual.png");

TCanvas c8;

c8.cd(1);
h15->GetXaxis()->SetTitle("Cluster Average PE Count");
h15->GetYaxis()->SetTitle("Normalized Track No.");
h15->Draw("bar");
h15->Scale(1./h15->Integral());
h15->SetFillColorAlpha(kGreen,.35);
h16->SetFillColorAlpha(kRed,.4);
h16->Scale(1./h16->Integral());
h16->Draw("bar same");
TLegend *leg8 = c8.BuildLegend(.75,.75,1,1);
c8.SaveAs("ClusterAv.png");

TCanvas c9;

c9.cd(1);
h17->GetXaxis()->SetTitle("Tag PE Count");
h17->GetYaxis()->SetTitle("Normalized Track No.");
h17->Draw("bar");
h17->Scale(1./h17->Integral());
h17->SetFillColorAlpha(kGreen,.35);
h18->SetFillColorAlpha(kRed,.4);
h18->Scale(1./h18->Integral());
h18->Draw("bar same");
TLegend *leg9 = c9.BuildLegend(.75,.75,1,1);
c9.SaveAs("ClusterRes.png");

TCanvas c10;

c10.cd(1);
h20->GetXaxis()->SetTitle("Tag PE Count");
h20->GetYaxis()->SetTitle("Normalized Track No.");
h20->Draw("bar");
h20->Scale(1./h20->Integral());
h20->SetFillColorAlpha(kRed,.35);
h19->SetFillColorAlpha(kGreen,.4);
h19->Scale(1./h19->Integral());
h19->Draw("bar same");
TLegend *leg10 = c10.BuildLegend(.75,.75,1,1);
c10.SaveAs("ResponseCurves.png");

TCanvas c11;

c11.cd(1);
h21->GetXaxis()->SetTitle("Background Efficiency");
h21->GetYaxis()->SetTitle("Signal Efficiency");
h21->Draw("");
//h21->Scale(1./h20->Integral());
//h21->SetFillColorAlpha(kRed,.35);
TLegend *leg11 = c11.BuildLegend(.75,.75,1,1);
c11.SaveAs("ROCCurve.png");



}
