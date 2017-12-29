
import os,sys

sys.path.insert(0, '../../0_Model')
from SimulationWrapper_System_3_servers import *
import OptimizationProblem

#Create an instance of the optimization problem
OP = OptimizationProblem.OptimizationProblem()

#Fixed parameters (defined in OptimizationProblem.py):
# OP.p  #arrival probability
# OP.K1 #num of servers in node 1
# OP.q2 #service prob  in node 2
# OP.alpha  #routing probability
# OP.W  #weight assigned to cost during optimization


import random
import time
import numpy as np
from scipy.optimize import fmin_cobyla


#remove duplicate entries from a list
def remove_duplicates(list_x):
    x = list_x[:]
    for i in range(len(x)):
        if(i>=len(x)):
            break
        for j in range(len(x)):
            if(j>=len(x)):
                break
            if(i!=j and x[i]==x[j]):
                del x[j]
    return x
                
#generate an array of initial guesses 
#and store it in a file:
def generate_initial_guesses(num_guesses, dimensions,bounds):

    random.seed(1)
    initial_guesses=[]
    while (len(initial_guesses)<num_guesses):
        #add a row
        initial_guesses.append([])
        #populate it
        for j in range(dimensions):
            initial_guesses[-1].append(random.randint(bounds[j][0],bounds[j][1]))
        #remove duplicates
        initial_guesses = remove_duplicates(initial_guesses)

    print "Initial guesses: (",len(initial_guesses),")",initial_guesses
    #store the array to a file:
    initial_guesses_file = open("Initial_guesses.py", "w")
    print >>initial_guesses_file, "initial_guesses=",
    print >>initial_guesses_file, initial_guesses
    initial_guesses_file.close()



#Run the following only once to generate the initial guesses:
generate_initial_guesses(num_guesses=1000, dimensions=OP.NUM_DIMENSIONS, bounds=OP.bounds)


