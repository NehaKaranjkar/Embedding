# Server_Geo.py
#
# A server with geometrically distributed service times.

import random
import simpy

from Job import Job
from Buffer import Buffer, EmbeddedBuffer
from Source_Geo import Source_Geo

class Server_Geo():
    
    def __init__(self, env, name, service_probability, inp):

        self.env=env
        self.name=name
        assert(service_probability>=0 and service_probability<=1)
        self.service_probability=service_probability
        assert(isinstance(inp,Buffer))
        self.inp=inp

        #stats
        self.num_jobs_served=0
        self.average_job_cycle_time=0
        self.average_throughput=0
        
        #start behavior
        self.process=env.process(self.behavior())

    def behavior(self):
        
        while(True):
            #wait until (near) the end of a slot
            yield (self.env.timeout(0.9))

            #check if there's a job to be served in the queue
            if(self.inp.can_get()):
                
                # with probability = service_probability,
                # finish serving the job at the front of the queue
                if(random.random()<self.service_probability):

                    job = self.inp.get()
                    t_total = float(self.average_job_cycle_time) * float(self.num_jobs_served)
                    t_total += (self.env.now+0.1)-job.timestamp
                    self.num_jobs_served +=1
                    self.average_job_cycle_time = t_total/self.num_jobs_served
                    #print("T=", self.env.now+0.0, self.name,"served job",job,"from",self.inp)
            
            #wait till the end of this slot
            yield (self.env.timeout(0.1))

            #compute avg throughput
            self.average_throughput = float(self.num_jobs_served)/float(self.env.now)


def Test1():
    env=simpy.Environment()
    B = Buffer()
    B.capacity=5
    Source_Geo(env,"Source",0.5,B)
    Server_Geo(env,"Server",0.6,B)
    env.run(until=20)

from Gamma import *

def Test2():
    env=simpy.Environment()
    gamma = Gamma([2,3],[0.4,0.6])
    B = EmbeddedBuffer(env,gamma)
    Source = Source_Geo(env,"Source",0.6,B)
    Server = Server_Geo(env,"Server",0.2,B)
    env.run(until=20)
    print ("Buffer average length = ",B.average_length)
    print ("Average throughput = ",Server.average_throughput)
    print ("Blocking probability = ",Source.blocking_probability)

#Test1()
#Test2()
