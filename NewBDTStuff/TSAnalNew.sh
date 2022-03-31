#!/bin/bash
source ./ldmx-sw/scripts/ldmx-env.sh

counter1=0
for word in $(ls "/nfs/slac/g/ldmx/data/mc21/v12/4.0GeV/v3.0.0-3e/")
	#28.926)
	do
	echo $word
	echo $counter1
	if [ $counter1 -lt 40 ]
	then
		#bsub -R "select[centos7]" -W 300 singularity run -B ${PWD}:${PWD} -B ${PWD}:${PWD} --home ${PWD} /nfs/slac/g/ldmx/production/singularityImages/ldmx-pro_v3.0.0-gLDMX.10.2.3_v0.4-r6.22.00-onnx1.3.0-xerces3.2.3-ubuntu18.04.sif . 
		ldmx fire runTSTrackanalysisNew.py "clustered_truth_${word}"
		wait $!
		counter1=$((counter1+1))
	fi
done

