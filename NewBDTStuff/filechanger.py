import re
import numpy as np
import matplotlib.pyplot as plt
import sys

#sys.argv[i] establishes the value of the ith gdml constant desired

#Establishes which ldmx configuration file to open
f=open(r'./EvalRes.C',"r")
#f=open(r'../ldmx-sw/Detectors/data/ldmx-det-v12/scoring_planes.gdml',"r")
ta=[n for n in f]
f.close()
N=int(sys.argv[1])
inputf=["oneAllW7.root","twoAllW7.root","threeAllW7.root","fourAllW7.root"]
ta[33]=ta[33][:28]+inputf[N]+"\");\n"
ta[46]=ta[46][:24]+str(N+1)+ta[46][25:]
ta[74]=ta[74][:12]+str(N+1)+ta[74][13:]
f=open(r'./EvalRes.C',"w")
for a in ta:
    f.write(a)
