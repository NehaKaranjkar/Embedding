# Job.py
#
# A single job with a timestamp

class Job():
   
    def __init__(self, timestamp=0, ID=0):

        self.timestamp=timestamp
        self.ID=ID
    
    def __str__(self):
        return "Job_"+str(self.timestamp)+"_"+str(self.ID)
        
