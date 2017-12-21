#Optimize using COBYLA

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
#generate_initial_guesses(num_guesses=100, dimensions=OP.NUM_DIMENSIONS, bounds=OP.bounds)


#read initial guesses into an array
import Initial_guesses
initial_guesses = Initial_guesses.initial_guesses
NUM_TRIALS=len(initial_guesses)


#Python list to store the results
RESULTS=[]
from collections import namedtuple
Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')


#Lengths of Simulation runs
simulation_budget = [1000, 10000, 100000, 1000000]
sim_length_best = max(simulation_budget)


def Run_COBYLA(embedding_method):

    #select the method used for 
    #embedding the discrete parameter space
    #into a continuous one.
    #
    #Eg: randomization_embedding,
    #   simplex_interpolation
    #   rounding
    OP.embedding_method=embedding_method
    
    for l in range(len(simulation_budget)) :
        
        OP.sim_budget = simulation_budget[l]
        simulation_length = embedding_method.get_simulation_length(simulation_budget[l])
        print "Simulation budget per point = ",simulation_budget[l]," simulation length = ",simulation_length
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
            x_opt = fmin_cobyla(func=OP.ObjectiveFunction, 
				x0=x_start,
				cons=OP.constraints,
                                iprint=0,
				rhobeg=5,
				rhoend=1e-3)
            t_end=time.time()

            #round x_opt to the nearest decimal point
            x_opt = OP.Round(x_opt)
            
            #compute results, using the best possible simulation_length:
            OP.sim_length = sim_length_best

            fevals = OP.objective_function_count 
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
    fname = "RESULTS_COBYLA_"+embedding_method.name+".py"
    print " Printing results to file",fname,"..."
    results_file = open(fname, "w")
    print >>results_file, "from collections import namedtuple"
    print >>results_file, "Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')"
    print >>results_file, "RESULTS=",RESULTS
    print " Done."
    print " ==============================================================="
    results_file.close()


def Summarize_results(result_filename):
    imp = __import__(result_filename)
    R = imp.RESULTS
    for i in range(len(R)):
        print ""
        print "Sim budget =",simulation_budget[i],"simulation length = ", OP.embedding_method.get_simulation_length(simulation_budget[i]),
        
        fopt = [ R[i][j].f_opt for j in range(len(R[i]))]
        fevals = [ R[i][j].f_opt for j in range(len(R[i]))]
        times = [ R[i][j].f_opt for j in range(len(R[i]))]
        
        print "fopt best=",min(fopt),
        print "fopt worst=",max(fopt),
        print "fopt avg=",np.mean(fopt),
        print "fopt stdev=",np.std(fopt, ddof=1 if len(fopt)>1 else 0),

embedding_method = OptimizationProblem.Embedding_randomization()
Run_COBYLA(embedding_method)
Summarize_results("RESULTS_COBYLA_"+embedding_method.name)


