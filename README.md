This repo is a beginners guide to quick python-based analysis of LDMX trigger scintillator data. 
The code depends on a few packages: ROOT, uproot, matplotlib.pyplot, and numpy. If you have 
the LDMX container install, you will have all but uproot installed.  You can also instal all 
of these yourself without LDMX installed. If you want to install uproot into your container, 
you can build your own tag of ldmx/dev using the following Dockerfile.

```
FROM ldmx/dev:latest
RUN sudo apt-get install --no-cache pip && pip install uproot
```

Then build it with:

`docker build . -t ldmx/dev:uproot`

You will have to tell ldmx-env.sh that you want to use a different tag as well:

`source ldmx-sw/scripts/ldmx-env.sh . uproot`

NOTE: this recipe hasn't been tested...

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

