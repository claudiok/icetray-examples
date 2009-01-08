from icecube.icetray import *
from icecube import dataclasses

class UseRandom(I3Module):
    """
    This module class uses an I3RandomService to get doubles and put them in
    the frame.  Used to illustrate that the randomservice can be pure python
    (e.g. ConstantService) or wrapped cpp (I3GSLRandomService).

    *Parameters*:

    * **I3RandomService** - a random service instance
    * **PutWhere** - where to put the constructed doubles
    
    """
    def __init__(self, context):
        I3Module.__init__(self, context)
        self.AddParameter("I3RandomService", "the service", None)
        self.AddParameter("PutWhere", "where the doubles go", None)

    def Configure(self):
        self.rs = self.GetParameter("I3RandomService")
        self.where = self.GetParameter("PutWhere")

    def Physics(self, frame):

        rnd = self.rs.Gaus(0,1)
        d = dataclasses.I3Double(rnd)
        frame.Put(self.where, d)

        self.PushFrame(frame)


        
