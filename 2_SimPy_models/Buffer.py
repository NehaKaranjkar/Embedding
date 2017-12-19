# Buffer.py
# 
# A wrapper around SimPy's store resource class.
# Models an infinite/finite capacity FIFO buffer.
#
# Parameters:
#   capacity: the buffer cannot accept an element if its size >= capacity.
# if capacity==None, the capacity is assumed to be infinite


import random
from collections import deque

class Buffer():
    
    def __init__(self, name="Buffer", capacity=float('inf')):
      
        self.name=name
        self.capacity=capacity
        self.buf=deque([])
            
    def __str__(self):
        return self.name
    
    def get(self):
        assert(len(self.buf)>0)
        return self.buf.pop()
    
    def put(self,job):
        assert(len(self.buf)<self.capacity)
        self.buf.appendleft(job)

    def can_put(self):
        return True if(len(self.buf) < self.capacity) else False
    
    def can_get(self):
        return True if(len(self.buf)>0) else False


import simpy
from Gamma import Gamma 

class EmbeddedBuffer(Buffer):
    
    def __init__(self, env, capacity_random_variable,name="Buffer"):
        self.env=env
        self.name=name
        assert(isinstance(capacity_random_variable,Gamma))
        self.capacity_random_variable=capacity_random_variable
        super(EmbeddedBuffer, self).__init__()
        
        #stats:
        self.average_length=0.0
        
        #start behavior
        self.process=env.process(self.behavior())

    def size(self):
        return len(self.buf)
    
    def behavior(self):

        while(True):
            
            #At the start of a slot,
            #perturb the capacity parameter:
            self.capacity = self.capacity_random_variable.get()
            #print("T=", self.env.now+0.0, self.name,"instantaneous capacity = ",self.capacity," size=",self.size())

            #at the end of a slot,
            yield (self.env.timeout(1))
            
            #update the verage queue length stats
            total_length = self.average_length*float(self.env.now-1.0) + len(self.buf)
            self.average_length = total_length/float(self.env.now)


def TestBuffer():
    B = Buffer()
    B.capacity=10

    for i in range(20):
        if not B.can_put():
            break
        B.put(i)
    while(B.can_get()):
        print (B.get())

    B.capacity=15

    for i in range(20):
        if not B.can_put():
            break
        B.put(i)
    while(B.can_get()):
        print (B.get())

