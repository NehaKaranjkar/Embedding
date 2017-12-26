#Optimize using SPSA

import os,sys

sys.path.insert(0, '../../0_Model')
from SimulationWrapper_System_3_servers import *

sys.path.insert(0, '../0_Optimization_problem')
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
#from scipy.optimize import fmin_cobyla
from noisyopt import minimizeSPSA


#read initial guesses into an array
import Initial_guesses
initial_guesses = Initial_guesses.initial_guesses
NUM_TRIALS=100


#Python list to store the results
RESULTS=[]
from collections import namedtuple
Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')


#Lengths of each Simulation run
simulation_budget = [10000]
sim_length_best = max(simulation_budget)


def Run_SPSA():

    
    for l in range(len(simulation_budget)) :
        
        OP.sim_budget = simulation_budget[l]
        simulation_length = simulation_budget[l]
        print " Simulation length = ",simulation_length
        RESULTS.append([])


        for trial in range(NUM_TRIALS):
            
            #set simulation_length for this optimization:
            OP.sim_length = simulation_length

            print "\tOptimization Run = ",trial,
            x_start = initial_guesses[trial]

            #clear the count of objective function evaluations.
            OP.objective_function_count=0
            
            t_start = time.time()

            #perform an optimization run
            res  = minimizeSPSA(func=OP.ObjectiveFunction, 
				x0=x_start,
                                bounds=OP.bounds,
                                paired=False,
                                niter=500,
				disp=False)
            t_end=time.time()

            #round x_opt to the nearest decimal point,
            #and clip it to lie within the domain 
            
            x_opt = OP.Round(OP.Clip(res.x))
            
            #compute results, using the best possible simulation_length:
            OP.sim_length = sim_length_best

            fevals = OP.objective_function_count-1 
            f_opt = OP.ObjectiveFunction(x_opt)
            throughput_opt = OP.NormalizedThroughput(x_opt)
            cost_opt = OP.NormalizedCost(x_opt)
            opt_time = t_end - t_start
            
            print "\t fevals = ", fevals,"\t time = ",opt_time
            
            #package the result into  a tuple
            R = Result(x_opt, f_opt, throughput_opt, cost_opt, fevals, opt_time)

            RESULTS[l].append(R)
    
    print " =============================================================="
    #write the Result array out to a file
    fname = "RESULTS_SPSA.py"
    print " Printing results to file",fname,"..."
    results_file = open(fname, "w")
    print >>results_file, "from collections import namedtuple"
    print >>results_file, "Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')"
    print >>results_file, "RESULTS=",RESULTS
    print " Done."
    print " ==============================================================="
    results_file.close()


def Summarize_results():
    result_filename = "RESULTS_SPSA"
    imp = __import__(result_filename)
    R = imp.RESULTS
    
    fname = "RESULTS_SPSA_summary.txt"
    output_file = open(fname, 'w+')
    for i in range(len(R)):
        
        fopt = [ R[i][j].f_opt for j in range(len(R[i]))]
        fevals = [ R[i][j].fevals for j in range(len(R[i]))]
        times = [ R[i][j].time for j in range(len(R[i]))]
        
        print >>output_file, ""
        print >>output_file, "Simulation length = ", simulation_budget[i],
        print >>output_file,"fopt best=",min(fopt),
        print >>output_file,"fopt worst=",max(fopt),
        print >>output_file,"fopt avg=",np.mean(fopt),
        print >>output_file,"fopt stdev=",np.std(fopt),
        
        print >>output_file,"fevals min=",min(fevals),
        print >>output_file,"fevals max=",max(fevals),
        print >>output_file,"fevals avg=",np.mean(fevals),
        print >>output_file,"fevals stdev=",np.std(fevals),
  
        print >>output_file,"times min=",min(times),
        print >>output_file,"times max=",max(times),
        print >>output_file,"times avg=",np.mean(times),
        print >>output_file,"times stdev=",np.std(times),
        #output_file.close()

#Run optimization
Run_SPSA()
Summarize_results()


