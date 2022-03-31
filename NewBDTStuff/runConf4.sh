#!/bin/bash
source ~/root_install/bin/thisroot.sh
wait $!
mkdir $1
#wait $!
#cp ../secondOrder.JPG $1/BDTRun.png
#wait $!
#cp ../ClusterResidualRun.root ./BDTVar.root
#cp ../$3 ./BDTVar.root
#wait $!
#THIS SECTION WILL COLATE ALL PICTURES ASSOCIATED WITH BDT VARIABLES
counter=0
for i in $(seq -.6 .01 .6)
do
	python filechanger2.py $i $counter $1
	wait $!
	root -q newHist5.C
	wait $!
	cp ./runRT$counter.png ./$1/runRT$counter.png
	wait $!
	rm ./runRT$counter.png
	wait $!
	counter=$((counter+1))
done
#python HTMLMaker.py $1 $2
wait $!
#rm selectedf5.root

