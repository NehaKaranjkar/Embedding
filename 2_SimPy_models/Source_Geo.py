# Source_Geo.py
#
# A source that creates jobs
# with Geometrically distributed inter-arrival times
# and outputs them into a buffer.

import random
import simpy

from Job import Job
from Buffer import Buffer

class Source_Geo():
    
    def __init__(self, env, name, arrival_probability, outp):

        self.env=env
        self.name=name
        assert(arrival_probability>=0 and arrival_probability<=1)
        self.arrival_probability=arrival_probability
        assert(isinstance(outp,Buffer))
        self.outp=outp

        #stats
        self.num_jobs_created=0
        self.num_jobs_lost=0
        self.blocking_probability=0
        
        #start behavior
        self.process=env.process(self.behavior())

    def behavior(self):
        
        while(True):
            
            #In this slot, a job gets created
            # with probability = arrival_probability
            if(random.random()<self.arrival_probability):
                
                #create a job and timestamp it
                job = Job(self.env.now)
                self.num_jobs_created +=1

                #wait for a delta amount of time
                yield (self.env.timeout(0.1))

                #check if there's place at the output buffer
                if (self.outp.can_put()):
                    #output the job
                    self.outp.put(job)
                    #print("T=", self.env.now+0.0, self.name,"output job",job,"to",self.outp)
                else:
                    self.num_jobs_lost+=1
                
                self.blocking_probability = float(self.num_jobs_lost)/float(self.num_jobs_created)
                #wait till the end of the slot
                yield (self.env.timeout(0.9))
            
            else:
                #wait till the next slot
                yield (self.env.timeout(1))

def Test():
    env=simpy.Environment()
    B = Buffer()
    B.capacity=5
    Source_Geo(env,"Source",0.8,B)
    env.run(until=20)
