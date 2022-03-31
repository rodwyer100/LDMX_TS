#!/usr/bin/python                                                                                                                                                  
import sys
import os
                                                                                             
from LDMX.Framework import ldmxcfg
                                                                               
passName="truth"
p=ldmxcfg.Process( passName )
simPassName="sim" #<-- whatever is in the input, if those collections would be used for anything, instead of the pass created here
#maximum number of events to process                                                                                                                               
nEv = 10000

if len(sys.argv) >= 2 :
    inputName=sys.argv[1]  #specify the input name                                                                                       
else:
     #inputName=sys.argv[0]
     print("An input file name has to be specified. Use (positional) argument 2 for it.")
     exit(1)
     #inputName="NonRotarun1-eout.root"
print("Using input file name: "+inputName)

if len(sys.argv) >= 3 :
    outputName=sys.argv[2]  #specify the output name if default is not desired                                                                                     
else:
    outputName="clustered_truth_"+inputName
print("Using output file name: "+outputName)

#setup a log file 
#lFileName = outputName.replace(".root", ".log")
#p.logFileName= lFileName
#p.fileLogLevel=0     # 0: debug, 1: info, 2: warning, 3: error, 4: fatal... i think. 
p.termLogLevel=0     # same here. pick the severity needed to print something to log/stdout
# ------------------- all set; propagate these settings in detail, and run  ---------------                                                                        
#load the default configuration files                                                                                                                              
from LDMX.TrigScint.trigScint import TrigScintDigiProducer
from LDMX.TrigScint.trigScint import TrigScintClusterProducer
from LDMX.TrigScint.trigScint import trigScintTrack
from LDMX.TrigScint.trigScint import TrigScintTrackProducer
from LDMX.TrigScint.truthHits import TruthHitProducer
#-- create truth beam electron collections                                                                                                                         
beTag=TruthHitProducer.tagger()
#beTag.pass_name="sim"
beUp=TruthHitProducer.up()
#beTag.pass_name="sim"
beDown=TruthHitProducer.down()
#beTag.pass_name="sim"
#-- digi of truth beam electron collections                                                                                                                        
digiTag=TrigScintDigiProducer.tagger()
digiUp=TrigScintDigiProducer.up()
digiDown=TrigScintDigiProducer.down()
# --- set the resulting collections as input for the next step
# (could use: digiTag.output_collection (or whatever the variable is called))
digiTag.input_collection="truthBeamElectronsTag"                                                                                                                  
#digiTag.pass_name=passName
digiUp.input_collection="truthBeamElectronsUp"
#digiUp.pass_name=passName
digiDown.input_collection="truthBeamElectronsDn"
#digiDown.pass_name=passName
#turn off noise hits in truth collections                                                                                                                          
digiTag.mean_noise=0.00000000001
digiUp.mean_noise=0.00000000001
digiDown.mean_noise=0.000000001
# --- clustering ---
clTag=TrigScintClusterProducer.tagger()
clUp=TrigScintClusterProducer.up()
clDown=TrigScintClusterProducer.down()
# --- input hits to clustering are made in this pass
clTag.input_pass_name=passName
clUp.input_pass_name=passName
clDown.input_pass_name=passName

clTag.time_tolerance=.5
clUp.time_tolerance=.5
clDown.time_tolerance=.5

# --- tracking ---
trigScintTrack.input_pass_name=passName
p.maxEvents=nEv
p.sequence = [ beTag, beUp, beDown] 
p.sequence.extend( [digiTag, digiUp, digiDown, clTag, clUp, clDown, trigScintTrack ])

# Provide the list of input files to run on
p.inputFiles=[ inputName ]
p.outputFiles=[outputName]

# Utility function to interpret and print out the configuration to the screen                                                                                      
print(p)
