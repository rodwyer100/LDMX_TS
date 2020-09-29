This repo is a beginners guide to quick python-based analysis of LDMX trigger scintillator data. 
The code depends on a few packages: [ROOT](https://root.cern.ch/downloading-root), [uproot](https://github.com/scikit-hep/uproot#jagged-array-performance), [matplotlib](https://matplotlib.org/3.2.1/users/installing.html), and [numpy](https://numpy.org/install/). If you use the `unification` LDMX container, you can access all of these, as well as run `ldmx-sw`, by prepending `ldmx` to all your normal commands. 

To set up the container, run

`source [path-to-ldmx-sw]/ldmx-sw/scripts/ldmx-env.sh -r dev -t unification -b [path-to-ldmx-sw] `

(where `-b` is the path to the `ldmx-sw` base dir (defaults to `pwd`), `-r` is for repo (for completeness, these can be `dev` (this is what we want), `local` (for something you built yourself), `pro` (for sample production tags)), and `-t` is for `tag`).


NOTE that `[path-to-ldmx-sw]` should be replaced with any (relative) path to the directory where the `ldmx-sw` directory is located in your setup, or `.` for the present working directory (`pwd`). Run this command **every time** you want to run analysis from a fresh shell.

The code is setup such that `ts_digi_container.py` should be used load the tree and
extract information from the tree. In general, users can use the `get_data`
method to pull data from the tree. This function will get an arbitrary branch from 
the tree user should pass the collection and the data member separately.  Don't include
the '_' that is printed at the end of the branch name when one executes `TTree::Show`.
For example you could run the following to get all ECal sim hits.  

```
get_data('EcalSimHits_sim','edep') # get edep for all events and all sim hits
get_data('EcalSimHits_sim','edep',10) # get edep for the 11th event and all sim hits
```

There are also other helpful function that automate various common calculations.  
In general, functions are written to either pass data from all events, when `event=-1`,
or a single event.  There are some cases where its difficult or impossible to extract 
data for all event simultaneously.  You can distinguish these by checking the defualt
value `event` in the method's definition.

## Running the analysis code with the container

The example script is written in python, and to run it inside the container, just prepend your normal `python` command with `ldmx`:

`ldmx python test_analyzer.py`

Remember that the container is a little bit of a universe of its own. When it gets set up, the setup script mounts your working directory on the container behind the scenes -- but it can't see your entire file system. Be mindful of this if you try to run scripts that are on completely different paths; either copy them over, or set up the container in that path (pro tip: use a fresh shell for this). 


## Running event simulation with ldmx-sw

You can produce your own events using the runSimAndDigi.py script.

Run it (after sourcing the env script as indicated above, if you're in a fresh shell) as:

`ldmx fire runSimAndDigi.py [number of electrons per event] [optional: run number] [optional: output file name base]`

The first argument is mandatory.
Inside the script, you can also change the number of events generated, or if you want to use a fix electron multiplicity per event (default and easiest) or if it should be varied according to a Poisson distribution around the number you specified. Be mindful that a large number of events/electron multiplicity both lead to longer simulation time and larger output files. 




## Running clustering and tracking on a simulated file 
`ldmx fire runClusteringAndTracking.py [nElectrons] [input file] [output file]`

Here the number of electrons is not really used for anything but some default naming stuff. So it might get removed. 
You can for example use `test.root` as input file. You might need to change the pass name in 

`p=ldmxcfg.Process("digi")`
to something else than "digi", if this pass already exists.


