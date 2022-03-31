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

void newHist6(){
TFile *myFile=TFile::Open("./selected3.root");//"autorunout33.root");
TH2D *h1 = new TH2D("h1","h1",8,0,8,8,0,8);	
TH2D *h2 = new TH2D("h2","h2",8,0,8,8,0,8);	
TH2D *h3 = new TH2D("h3","h3",8,0,8,8,0,8);	
//TH2D *h4 = new TH2D("h4","h4",8,0,8,8,0,8);	
TTreeReader myReader("selected;1",myFile);
//cout<<myFile->GetListOfKeys()->At(0)->GetName()<<endl;
TTreeReaderArray<Int_t> nTracks(myReader,"nTracks");
TTreeReaderArray<Float_t> BDT(myReader,"BDT");
TTreeReaderArray<Float_t> realT(myReader,"TrueTrack");TTreeReaderArray<Float_t> realT2(myReader,"RealTrack");
//TTreeReaderArray<Int_t> ndHits(myReader,"TriggerPadDownClusters_sim.nHits_");
Int_t counter=0.0;
//myReader.Print();
int helper[5][8];
Float_t fillN=0.0;
Float_t lastTrue=0.9;

while(myReader.Next()){
	//cout<<BDT.GetSize()<<endl;
	if(BDT[0]>0.51){
		//cout<<r
		if(isnan(BDT[0])){continue;}
		//cout<<BDT[0]<<endl;
		if(nTracks[0]==counter){
			fillN+=1.0;
			lastTrue=realT[0];
			//cout<<nTracks[0]<<endl;cout<<counter<<endl;	
		}else{
			if(nTracks[0]==0){
				//cout<<"hllo2"<<endl;
				if(lastTrue==1){
					h1->Fill(lastTrue,0.0);fillN=0.0;counter=-1;lastTrue=realT[0];}
				if(lastTrue==2){
					h2->Fill(lastTrue,0.0);fillN=0.0;counter=-1;lastTrue=realT[0];}
				if(lastTrue==3){
					h3->Fill(lastTrue,0.0);fillN=0.0;counter=-1;lastTrue=realT[0];}		
				//if(lastTrue==4){
				//	h4->Fill(lastTrue,0.0);fillN=0.0;counter=-1;lastTrue=realT[0];}
			}else{	
				//cout<<nTracks[0]<<endl;
				if(lastTrue==1){
					h1->Fill(lastTrue,fillN);fillN=1.0;counter=nTracks[0];lastTrue=realT[0];}
				if(lastTrue==2){
					h2->Fill(lastTrue,fillN);fillN=1.0;counter=nTracks[0];lastTrue=realT[0];}
				if(lastTrue==3){
					h3->Fill(lastTrue,fillN);fillN=1.0;counter=nTracks[0];lastTrue=realT[0];}
				//if(lastTrue==4){
				//	h4->Fill(lastTrue,fillN);fillN=1.0;counter=nTracks[0];lastTrue=realT[0];}
			}
		}
	}
}
Double_t scale=1./(h1->Integral());
//h1->Scale(scale);
//scale=1./(h2->Integral());
//h2->Scale(scale);
//scale=1./(h3->Integral());
//h3->Scale(scale);
//scale=1./(h4->Integral());
//h4->Scale(scale);
TCanvas c1;
c1.cd(1);
h1->GetXaxis()->SetTitle("Expected Number");
h1->GetYaxis()->SetTitle("Num Tracks");
gPad->SetLogz();
h1->SetTitle("Confusion Matrix for BDT value of 0.51");
h1->Draw("colz text");

h2->GetXaxis()->SetTitle("Expected Number");
h2->GetYaxis()->SetTitle("Num Tracks");
h2->SetTitle("Confusion Matrix for BDT value of -0.22");
h2->Draw("colz text same");

h3->SetTitle("Confusion Matrix for BDT value of -0.22");
h3->GetXaxis()->SetTitle("Expected Number");
h3->GetYaxis()->SetTitle("Num Tracks");
h3->Draw("colz text same");

//h4->GetXaxis()->SetTitle("Expected Number");
//h4->GetYaxis()->SetTitle("Num Tracks");
//h4->SetTitle("Confusion Matrix for BDT value of -0.22");
//h4->Draw("colz text same");
c1.SaveAs("run111.png");

myFile->Close();

}
