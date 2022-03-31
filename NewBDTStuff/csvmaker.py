import ROOT
import csv
f = ROOT.TFile("ResidiAvBackW6.root")
f2 = ROOT.TFile("ResidiAvSigW6.root")
myTree = f.Get("t1;1")
myTree2 = f2.Get("t1;1")
csvfile=open('ResidiAvBackW6.csv','w',newline='')
writer=csv.DictWriter(csvfile,fieldnames=['clPEUp1','clPEDn1','clPETag1','residual','clTimeUp','clTimeDn','clTimeTag','nTracks','clusterAv','clusterRes','TrueTrack'])
writer.writeheader()
for entry in myTree:
    writer.writerow({'clPEUp1':entry.clPEUp1,'clPEDn1':entry.clPEDn1,'clPETag1':entry.clPETag1,'residual':entry.residual,'clTimeUp':entry.clTimeUp,'clTimeDn':entry.clTimeDn,'clTimeTag':entry.clTimeTag,'nTracks':entry.nTracks,'clusterAv':entry.clusterAv,'clusterRes':entry.clusterRes,'TrueTrack':entry.TrueTrack})
#,newline=''
csvfile2=open('ResidiAvSigW6.csv','w',newline='')
writer2=csv.DictWriter(csvfile2,fieldnames=['clPEUp1','clPEDn1','clPETag1','residual','clTimeUp','clTimeDn','clTimeTag','nTracks','clusterAv','clusterRes','TrueTrack'])
writer2.writeheader()
for entry in myTree2:
    writer2.writerow({'clPEUp1':entry.clPEUp1,'clPEDn1':entry.clPEDn1,'clPETag1':entry.clPETag1,'residual':entry.residual,'clTimeUp':entry.clTimeUp,'clTimeDn':entry.clTimeDn,'clTimeTag':entry.clTimeTag,'nTracks':entry.nTracks,'clusterAv':entry.clusterAv,'clusterRes':entry.clusterRes,'TrueTrack':entry.TrueTrack})
#  

#    print(entry.clPEUp1)
#    print(entry.clPEDn1)
#    print(entry.clPETag1)
#    print(entry.residual)
#    print(entry.clTimeUp)
#    print(entry.clTimeDn)
#    print(entry.clTimeTag)
#    print(entry.nTracks)


