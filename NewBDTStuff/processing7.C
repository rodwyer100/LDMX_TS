#include <stdio.h>
#include <math.h>
#include <sstream>
#include "TFile.h"
#include "TTree.h"
#include "TTreeReader.h"
#include "TTreeReaderArray.h"
#include <fstream>
#include <iostream>
#include <iomanip>


int processing7(){

TFile *myFile=TFile::Open("result1Ttracksig.root");
myFile->ls();
TDirectory* dir = myFile->GetDirectory(myFile->GetListOfKeys()->At(0)->GetName());
//dir->ls();
TTreeReader myReader1("TrigScintHits",dir);
TTreeReader myReader2("tracks",dir);
TTreeReader myReader3("hits",dir);
TTreeReader myReader4("clusters",dir);
TTreeReaderArray<Float_t> nTracks(myReader1,"nTracks");
TTreeReaderArray<Float_t> resid(myReader2,"residual");
TTreeReaderArray<Float_t> tTrk(myReader2,"tTrk");
TTreeReaderArray<Float_t> beamEfrac(myReader2,"beamEfrac");
TTreeReaderArray<Float_t> truthDY(myReader2,"truthDeltaY");
TTreeReaderArray<Float_t> hitEtag(myReader3,"hitEnergyTag");
TTreeReaderArray<Float_t> hitEup(myReader3,"hitEnergyUp");
TTreeReaderArray<Float_t> hitEDn(myReader3,"hitEnergyDn");
TTreeReaderArray<Float_t> clPEUp(myReader4,"clPEUp");
TTreeReaderArray<Float_t> clPEDn(myReader4,"clPEDn");
TTreeReaderArray<Float_t> clPETag(myReader4,"clPETag");
TTreeReaderArray<Float_t> clTimeUp(myReader4,"clTimeUp");
TTreeReaderArray<Float_t> clTimeTag(myReader4,"clTimeTag");
TTreeReaderArray<Float_t> clTimeDn(myReader4,"clTimeDn");
TTreeReaderArray<Float_t> nHitsDn(myReader4,"nHitsDn");
TTreeReaderArray<Float_t> hitXUp(myReader3,"hitXUp");
TTreeReaderArray<Float_t> hitXDn(myReader3,"hitXDn");
TTreeReaderArray<Float_t> hitXTag(myReader3,"hitXTag");
TTreeReaderArray<Float_t> hitYUp(myReader3,"hitYUp");
TTreeReaderArray<Float_t> hitYDn(myReader3,"hitYDn");
TTreeReaderArray<Float_t> hitYTag(myReader3,"hitYTag");


TTreeReaderArray<Float_t> hitBarIDUp(myReader3,"hitBarIDUp");
TTreeReaderArray<Float_t> hitBarIDDn(myReader3,"hitBarIDDn");
TTreeReaderArray<Float_t> hitBarIDTag(myReader3,"hitBarIDTag");
TTreeReaderArray<Float_t> hitTimeUp(myReader3,"hitTimeUp");
TTreeReaderArray<Float_t> hitTimeDn(myReader3,"hitTimeDn");
TTreeReaderArray<Float_t> hitTimeTag(myReader3,"hitTimeTag");

//TFile *myFile2=TFile::Open("result4NEWWWTsig.root");
//myFile2->ls();
//TDirectory* dir2 = myFile2->GetDirectory(myFile2->GetListOfKeys()->At(0)->GetName());
//dir->ls();
//TTreeReader myReader5("tracks",dir2);
//TTreeReaderArray<Float_t> beamEfrac2(myReader5,"beamEfrac");

TFile f("ResidiAvTtrackback.root","recreate");
TTree t1("t1","processedsig");
Float_t nTracksN;
//Float_t residN1;
Float_t clPEUpN1;
Float_t clPEDnN1;
Float_t clPETagN1;
Float_t residN1;

//Float_t hitBarIDUpN1; 
//Float_t hitBarIDDnN1;
//Float_t hitBarIDTagN1;
Float_t clTimeUpN1;
Float_t clTimeDnN1;
Float_t clTimeTagN1;
Float_t hitXSpeedUpN1;
Float_t clusterAv;
Float_t clusterRes;
Float_t truthDeltaY;
Float_t TrueTrack;

//Float_t hitsUpxN;
//Float_t hitsUpyN;
//Float_t hitsDnxN;
//Float_t hitsDnyN;
//Float_t hitsTagxN;
//Float_t hitsTagyN;
//Float_t clPEDnN;
//Float_t nHitsDnN;
//Float_t slope1;
//Float_t slope2;
//t1.Branch("nTracks",&nTracksN,"a");
//t1.Branch("residual1",&residN1,"a");
t1.Branch("clPEUp1",&clPEUpN1,"b");
t1.Branch("clPEDn1",&clPEDnN1,"c");
t1.Branch("clPETag1",&clPETagN1,"d");
t1.Branch("residual",&residN1,"e");
//t1.Branch("hitBarIDDn",&hitBarIDDnN1,"f");
//t1.Branch("hitBarIDTag",&hitBarIDTagN1,"g");
t1.Branch("clTimeUp",&clTimeUpN1,"h");
t1.Branch("clTimeDn",&clTimeDnN1,"i");
t1.Branch("clTimeTag",&clTimeTagN1,"j");
t1.Branch("nTracks",&nTracksN,"k");
t1.Branch("clusterAv",&clusterAv,"l");
t1.Branch("clusterRes",&clusterRes,"m");
t1.Branch("truthDeltaY",&truthDeltaY,"o");
t1.Branch("TrueTrack",&TrueTrack,"n");
//t1.Branch("hitXSpeedUp",&hitXSpeedUpN1,"k");
//t1.Branch("hitsUpx",&hitsUpxN,"e");
//t1.Branch("hitsUpy",&hitsUpyN,"f");
//t1.Branch("hitsUpx",&hitsDnxN,"g");
//t1.Branch("hitsUpy",&hitsDnyN,"h");
//t1.Branch("hitsUpx",&hitsTagxN,"i");
//t1.Branch("hitsUpy",&hitsTagyN,"j");

//t1.Branch("clTimeUp",&clTimeUpN,"d");
//t1.Branch("nHitsDn",&nHitsDnN,"e");

//t1.Branch("slope1",&slope1,"h");
//t1.Branch("slope2",&slope2,"i");

//clusters->Draw("clTimeUp>>h(100,-.01,.005)","","colz");
//TH1 *h1=new TH1D("h1","h1",4,-.1,4);
//TH1 *h2=new TH1D("h2","h2",4,-.1,4);
//TH2 *h3=new TH2D("h3","h3",200,0,400,200,0,400);
//TH2 *h4=new TH2D("h4","h4",200,0,400,200,0,400);
Float_t counter=0;
while((myReader1.Next())and(myReader2.Next())and(myReader3.Next())and(myReader4.Next())){//and(myReader5.Next())){
	//cout<<nTracks[0]<<endl;
	//cout<<clPEUp[1]<<endl;
	//counter+=1;
	//if(clTimeUp[0]<.001){
	//cout<<nTracks[0]<<endl;
	//nTracksN=(int) nTracks[0];
	bool helper=true;
	for(int I=0;I<beamEfrac.GetSize();I++){
		if(beamEfrac[I]<.99){
			helper = false;
		}
	}
	//helper=true;
	if(beamEfrac.GetSize()>1){
	//	helper = false;
		//cout<<beamEfrac.GetSize()<<endl;
	}
	//helper=true;
	//1636,1637
	//if(counter>1637){
	//	helper=false;
	//}
	if(counter==1636 or counter==1637){
		cout<<beamEfrac.GetSize()<<endl;
		cout<<resid.GetSize()<<endl;
		cout<<clPEUp.GetSize()<<endl;
		cout<<clPEDn.GetSize()<<endl;
		cout<<clPETag.GetSize()<<endl;
		//cout<<hitTimeUp.GetSize()<<endl;
		//cout<<hitTimeDn.GetSize()<<endl;
		//cout<<hitTimeTag.GetSize()<<endl;
	}
	if(beamEfrac.GetSize()==0){
		nTracksN=0;
		residN1=-.1;
		clPEUpN1=-.1;
		clPEDnN1=-.1;
		clPETagN1=-.1;
		clTimeUpN1=-5;
		clTimeDnN1=-5;
		clTimeTagN1=-5;
		clusterAv=-1;
		clusterRes=-1;
		truthDeltaY=-1;
		TrueTrack=0;
		t1.Fill();

	}
	for(int J=0;J<beamEfrac.GetSize();J++){
		//if((J>=clPEUp.GetSize())or(J>=clPEDn.GetSize())or(J>=clPETag.GetSize())){continue;}
		if(helper){
			nTracksN=counter;
			//cout<<beamEfrac.GetSize()<<endl;
			//nTracksN=nTracks[J];
			residN1=resid[J];
			clPEUpN1=clPEUp[J];
			clPEDnN1=clPEDn[J];
			clPETagN1=clPETag[J];
			clTimeUpN1=floor(clTimeUp[J]*2.0)/2.0;
			clTimeDnN1=floor(clTimeDn[J]*2.0)/2.0;
			clTimeTagN1=floor(clTimeTag[J]*2.0)/2.0;
			Float_t Av=(clPEUpN1+clPEDnN1+clPETagN1)/3.0;
			clusterAv=Av;
			clusterRes=sqrt(((clPEUpN1-Av)*(clPEUpN1-Av)+(clPEDnN1-Av)*(clPEDnN1-Av)+(clPETagN1-Av)*(clPETagN1-Av))/3.0);
			//if(clusterRes>1200000.0){
			//	clusterRes=1200000.0;
			//}
			truthDeltaY=truthDY[J];
			TrueTrack=tTrk[J];//cout<<counter<<endl;
			t1.Fill();
		}
	}
	counter+=1.0;
}
	//if(nTracks[0]==1){
	//	for(int k=0;k<nHitsDn.GetSize();k++){
	//		h1->Fill(nHitsDn[k]);
			//h4->Fill(clPEDn[k],clPEUp[k]);
	//	}
	//}
	//if(nTracks[0]==2){
	//	for(int k=0;k<nHitsDn.GetSize();k++){
	//		h2->Fill(nHitsDn[k]);
			//h3->Fill(clPEDn[k],clPEUp[k]);
	//	}
	//}
	//h1->Fill();
t1.Write();
return 0;	

}

