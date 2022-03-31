#!/bin/bash
hadd -f "selected.root" "selected1.root" "selected2.root"
wait $!
hadd -f "selectedn.root" "selected3.root" "selected4.root"
wait $!
hadd -f "selectedf5.root" "selected3.root" "selected.root"
#wait $!
#hadd -f "selected.root" "selected3.root" "selected.root"
wait $!
#hadd -f "selected.root" "selected4.root" "selected.root"
rm selectedn.root
rm selected.root

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
