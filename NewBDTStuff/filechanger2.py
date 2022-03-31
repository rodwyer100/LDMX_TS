import re
import numpy as np
import matplotlib.pyplot as plt
import sys

#sys.argv[i] establishes the value of the ith gdml constant desired

#Establishes which ldmx configuration file to open
f=open(r'./newHist5.C',"r")
#f=open(r'../ldmx-sw/Detectors/data/ldmx-det-v12/scoring_planes.gdml',"r")
ta=[n for n in f]
f.close()
N=float(sys.argv[1])
N2=int(sys.argv[2])
#print(ta[2])
#ta[45]=ta[45][:11]+str(N)+"){"


#ta[55]=ta[55][:11]+str(N)+"){\n"

ta[31]=ta[31][:11]+str(N)+"){\n"

ta[len(ta)-22]=ta[len(ta)-22][:48]+str(N)+"\");\n"

ta[len(ta)-5]=ta[len(ta)-5][:11]+"runRT"+str(N2)+".png\");\n"

#print(ta[45])
#print(ta[50])
#print(ta[len(ta)-22])
#print(ta[len(ta)-5])
#f=open(r'./probCompare.C',"w")
f=open(r'./newHist5.C',"w")
for a in ta:
    f.write(a)
f.close()
