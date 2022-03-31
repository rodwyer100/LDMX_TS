#!/bin/bash
source ./ldmx-sw/scripts/ldmx-env.sh

counter1=0
for word in $(ls "/nfs/slac/g/ldmx/data/mc21/v12/4.0GeV/v3.0.0-4e/")
	#28.926)
	do
	echo $word
	echo $counter1
	#sleep 10
	#word="mc_v12-4GeV-1e-inclusive_run10${j}_t1612471585.root"
	#if [ $j -lt 100]
	#then
	#	word="mc_v12-4GeV-1e-inclusive_run100${helper}_t1612471585.root" .
	#	
     	#	if [ $j -lt 10]
	#	then
	#		word="mc_v12-4GeV-1e-inclusive_run1000${helper}_t1612471585.root" .
		
	#	fi
	#fi
	if [ $counter1 -lt 40 ]
	then
		cp "/nfs/slac/g/ldmx/data/mc21/v12/4.0GeV/v3.0.0-4e/${word}" .
		wait $!
		bsub -R "select[centos7]" -W 300 singularity run -B ${PWD}:${PWD} -B ${PWD}:${PWD} --home ${PWD} /nfs/slac/g/ldmx/production/singularityImages/ldmx-pro_v3.0.0-gLDMX.10.2.3_v0.4-r6.22.00-onnx1.3.0-xerces3.2.3-ubuntu18.04.sif . runClusteringAndTracking.py 1 $word $word	
		counter1=$((counter1+1))	
	fi
done




#PUTS THE INFO FROM TSana from Each 10000 Event into One to Ship home
#ldmx root 'readPurpose5.C("'${word}'")'
#wait $!
#rm "./TSana_clustered_truth_${word}"
#counter=$counter+1


#v3 was 24, v4 21, v5 22.5, v6 22., v7 22.25i

#v8 all shifted down, v9 all shifted up

#v10 checks Dwn just in case

#v11 is the new config (thats all fucked)

#v13 is maybe the new config
