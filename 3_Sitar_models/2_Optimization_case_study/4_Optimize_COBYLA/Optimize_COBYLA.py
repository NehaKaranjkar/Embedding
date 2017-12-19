#Optimize using COBYLA

import os,sys

sys.path.insert(0, '../../0_Model')
from SimulationWrapper_System_3_servers import *

sys.path.insert(0, '../0_Optimization_problem')
import OptimizationProblem

#Create an instance of the optimization problem
OP = OptimizationProblem.OptimizationProblem()
OP.rand_seed=42 #rand seed used for each simulation


#Fixed parameters (defined in OptimizationProblem.py):
# OP.p  #arrival probability
# OP.K1 #num of servers in node 1
# OP.q2 #service prob  in node 2
# OP.alpha  #routing probability
# OP.W  #weight assigned to cost during optimization


#create some randomly chosen initial guesses:
NUM_TRIALS=100
initial_guesses = []

import random
random.seed(1)


for i in range(NUM_TRIALS):
    initial_guesses.append([])
    for j in range(OP.NUM_DIMENSIONS):
        initial_guesses[i].append(random.randint(OP.bounds[j][0],OP.bounds[j][1]))
#print "Initial guesses: ",initial_guesses

import numpy
from scipy.optimize import fmin_cobyla

#Python list to store the results
RESULTS=[]
from collections import namedtuple
Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')


#Lengths of Simulation runs
simulation_lengths = [10000,100000]


import time
import numpy as np


def Run_COBYLA():
    
    for l in range(len(simulation_lengths)) :
        print "Simulation length = ",simulation_lengths[l]
        OP.sim_length = simulation_lengths[l]
        RESULTS.append([])

        for trial in range(NUM_TRIALS):
            print "\tOptimization Run = ",trial,
            x_start = initial_guesses[trial]

            #clear the count of objective function evaluations.
            OP.objective_function_count=0
            
            t_start = time.time()

            #perform an optimization run
            x_opt = fmin_cobyla(func=OP.ObjectiveFunction, 
				x0=x_start,
				cons=OP.constraints,
                                iprint=0,
				rhobeg=2,
				rhoend=1e-3)
            t_end=time.time()

            #round x_opt to the nearest decimal point
            x_opt = OP.Round(x_opt)

            fevals = OP.objective_function_count 
            f_opt = OP.ObjectiveFunction(x_opt)
            throughput_opt = OP.NormalizedThroughput(x_opt)
            cost_opt = OP.NormalizedCost(x_opt)
            opt_time = t_end - t_start
            
            print "\t fevals = ", fevals,"\t time = ",opt_time
            
            #package the result into  a tuple
            R = Result(x_opt, f_opt, throughput_opt, cost_opt, fevals, opt_time)

            RESULTS[l].append(R)
    
    print " ========================================="
    print " Printing results to file RESULTS.py ..."
    #write the Result array out to a file
    results_file = open("RESULTS.py", "w")
    print >>results_file, "from collections import namedtuple"
    print >>results_file, "Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')"
    print >>results_file, "RESULTS=",RESULTS
    print " Done."
    print " ========================================="

#Run_COBYLA()



