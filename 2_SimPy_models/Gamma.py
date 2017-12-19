# Gamma is a discrete RandomVariable that represents
# the instantaneous values of a model parameter 
# to be embedded into continuous space

# parameters:
#
# stencil : list of values that the parameter takes
# alphas: probabilities of taking each value.
# For example, stencil = [2, 3] and alphas=[0.2, 0.8]
# means the random variable takes value 3 with prob 0.2
# and the value 3 with prob 0.8.


import numpy as np
import math
import random

class Gamma():

    def __init__(self, stencil, alphas):

        self.stencil = stencil
        self.alphas = alphas
        assert(len(stencil)>0)
        assert(len(alphas)==len(stencil))
        assert(sum(alphas)<=1.0+1e-6)#all probabilities should sum to 1

        #instantaneous and mean values
        self.value = self.stencil[0] 
        self.mean_value=sum([(stencil[i]*alphas[i]) for i in range(len(stencil))])
    

    #update and return the instantaneous value:
    def get(self):
        v = np.random.choice(self.stencil,p=self.alphas)
        self.value=v
        return v
        

def Test():
    gamma = Gamma([2,3,4],[0.4,0.4,0.2])
    for i in range(20):
        print (gamma.get())
    print("Mean=", gamma.mean_value)
