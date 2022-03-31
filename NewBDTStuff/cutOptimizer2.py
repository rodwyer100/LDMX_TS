import numpy as np
import ahoi
import csv

def getVal(a,b):
    return a[b[0],b[1],b[2],b[3]]#,b[4],b[5],b[6],b[7]]

csvfile=open('ResidiAvBackW6.csv',newline='')
csvfile2=open('ResidiAvSigW6.csv',newline='')


reader1=csv.reader(csvfile)
reader2=csv.reader(csvfile2)

inf1=[row for row in reader1]
info1=np.array(inf1)
#info1=[[float(info1[i][k]) for i in range(1,len(info1))] for k in range(len(info1[0]))]
inf2=[row for row in reader2]
info2=np.array(inf2)
#info2=[[float(info2[i][k]) for i in range(1,len(info2))] for k in range(len(info2[0]))]

#print(len(info2))
#print(len(info2[0]))
R=40
TopCombo=4
smd=0
v=[k/R for k in range(R)]#[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
shift=[1,1,1,0,-6,-6,-6,1,0,0,0]
mag=[400,400,400,.6,12,12,4,1000,0,0,0]
ITERA=5
def maxStage(a,b,n):
    if n==1:
        return max([a[i]/b[i] for i in range(len(b))])
    return max([maxStage(a[j],b[j],n-1) for j in range(len(a))])
#def maxFind(a,b,n,val,Max):
#    if n==TopCombo:
#        val=[-1 for g in range(TopCombo)]
#    if n==1:
#        if a[]-b[]==Max:
#            return val
for I in range(ITERA):
    masks_list10=[[[float(I) > mag[i+smd]*v[G]+shift[i+smd] for I in info1[1:50000,i+smd]] for G in range(int(len(v)))] for i in range(int(TopCombo))]
    masks_list20=[[[float(I) > mag[i+smd]*v[G]+shift[i+smd] for I in info2[1:50000,i+smd]] for G in range(int(len(v)))] for i in range(int(TopCombo))]
    #print("hello")
    #np.random.seed(42)
    #x=np.random.rand(10000,5)
    #masks_list1 =[[(sum([np.log((float(info1[k][:,i] > vv[k])+1.0)/2.0) for k in range(vv)])==0) for vv in v] for i in range(info1[1])]
    #masks_list2 =[[(sum([np.log((float(info2[k][:,i] > vv[k])+1.0)/2.0) for k in range(vv)])==0) for vv in v] for i in range(info2[1])]
    #masks_list2 = [[info1[:,i] > v for v in np.linspace(0,0.9,10)] for i in range(info2.shape[1])] 
    counts1 = ahoi.scan(masks_list10)
    #print(counts1[0,0,1,0])#,0,0,0,0])
    counts2 = ahoi.scan(masks_list20)
    #print(counts2[0,0,0,0])#,0,0,0,0])
    print(len(counts2))
    MAX = maxStage(counts1,counts2,TopCombo)
    #max([max([max([max([counts1[i,j,k,l]-counts2[i,j,k,l] for l in range(R)]) for k in range(R)]) for j in range(R)]) for i in range(R)])
    FirstMax = [-1 for j in range(TopCombo)]
    #FirstMax = []
    for i in range(R):
        for j in range(R):
            for k in range(R):
                for l in range(R):
                    #for m in range(R):
                        #for n in range(R):
                            #for o in range(R):
                                if counts1[i,j,k,l]/counts2[i,j,k,l]==MAX:
                                    FirstMax = [i,j,k,l]
                                break;
    print(FirstMax)
    print(shift)
    for i in range(TopCombo):
        shift[i+smd]=mag[i+smd]*v[FirstMax[i]]+shift[i+smd]-mag[i+smd]/2
    mag=[mag[i]/R for i in range(len(mag))]

#MAX = max([counts2-counts1 for k in range(len(counts1))])
#start=[0,0,0,0]#,0,0,0,0]

#for I in range(100):
#    value1=getVal(counts1,start)-getVal(counts2,start)
#    startN=[(start[i]+np.random.choice([-1,0,1]))%len(v) for i in range(len(start))]
#    print(value1)
#    print(startN)
#    value2=getVal(counts1,startN)-getVal(counts2,startN)
#    if value2<value1:
#        print("hello1")
#        continue
    #start=startN
    #print("hello2")
#print(start)
    #counts1[start[0],start[1],start[2],start[3],start[4],start[5],start[6],start[7]]
    
#for k in range(len(counts1)):
#    counts2[k]

