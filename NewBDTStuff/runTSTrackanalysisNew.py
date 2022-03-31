#!/usr/bin/python

import sys
import os
import json

# we need the ldmx configuration package to construct the object

from LDMX.Framework import ldmxcfg

# first, we define the process, which must have a name which identifies this
# processing pass ("pass name").
p=ldmxcfg.Process("anaTS")

p.inputFiles = [ sys.argv[1] ]

from LDMX.Analysis import ts2

ana=ts2.TSTrackAnalyzer2()
ana.passName="sim"
ana.rechit_collection="trigScintDigisTag" #RecHitsTagger_timeCut"
ana.truth_track_collection="TriggerPadTracks" 
ana.truth_passName="truth"
p.sequence = [ ana ]

p.termLogLevel = 2
#p.fileLogLevel = 0
#p.logFileName = sys.argv[1].replace(".root", ".log")

# set the maximum number of events to process
p.maxEvents=10000

# Provide the list of output files to produce
#   When using the simulator to produce events, only one output file is necessary
p.histogramFile='TSana_'+sys.argv[1]

# Utility function to interpret and print out the configuration to the screen
print(json.dumps(p.parameterDump(), indent=2))
#p.pause()
