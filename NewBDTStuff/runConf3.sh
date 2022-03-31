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
root -q BDTPlotter.C

wait $!
cp DownTime.png $1
rm DownTime.png
cp UpTime.png $1
rm UpTime.png
cp TagTime.png $1
rm TagTime.png
cp DownPE.png $1
rm DownPE.png
cp UpPE.png $1
rm UpPE.png
cp TagPE.png $1
rm TagPE.png
cp residual.png $1
rm residual.png
cp ClusterAv.png $1
rm ClusterAv.png
cp ClusterRes.png $1
rm ClusterRes.png
cp ResponseCurves.png $1
rm ResponseCurves.png
cp ROCCurve.png $1
rm ROCCurve.png

wait $!
#rm ./BDTVar.root
#wait $!
#THIS SECTION WILL COLATE THE CONFUSION MATRIX SCAN
for j in $(seq 0 1 3)
do
	python filechanger.py $j
	wait $!
	root -q EvalRes.C
	wait $!
done
wait $!
#. ./align.sh
##wait $!
#rm selected1.root
#rm selected2.root
#rm selected3.root
#rm selected4.root

#counter=0
#for i in $(seq -.6 .01 .6)
#do
#	python filechanger2.py $i $counter $1
#	wait $!
#	root -q newHist5.C
#	wait $!
#	cp ./run$counter.png ./$1/run$counter.png
#	wait $!
#	rm ./run$counter.png
#	wait $!
#	counter=$((counter+1))
#done
##python HTMLMaker.py $1 $2
#wait $!
##rm selectedf5.root

