import uproot

class ts_digi_container:
    def __init__(self,file_name='',tree_name=''):
        self.tree = uproot.open(file_name)[tree_name]
        self.digi_dm=["amplitude",
                      "energy",
                      "time",
                      "isNoise",
                      "pe",
                      "xpos","ypos","zpos",
                      "barID",
                      "beamEfrac"]

        self.data={}
        self.event_data={}
        self.cache={}
        self.NUM_CELLS=50

    def extend_branch_names(self,coll,branch_list):
        new_list=[]
        for branch in branch_list:
            new_list.append(coll+'.'+branch+'_')
        return new_list

    def get_digi_collection(self,coll):    
        self.data.update(self.tree.arrays(self.extend_branch_names(coll,self.digi_dm),cache=self.cache))

    def get_data(self,coll,data_member,event=-1):
        if event<0 : 
            return self.data[coll+'.'+data_member+'_']
        if event>=self.tree.numentries : 
            return None
        else : 
            return self.data[coll+'.'+data_member+'_'][event]
