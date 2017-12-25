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
NUM_TRIALS=1000


#Python list to store the results
RESULTS=[]
from collections import namedtuple
Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')


#Lengths of Simulation runs
simulation_budget = [100000]
sim_length_best = 1000000


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
				rhobeg=2,
				rhoend=1e-3)
            t_end=time.time()

            #round x_opt to the nearest decimal point,
            #and clip it to lie within the domain 
            x_opt = OP.Round(OP.Clip(x_opt))
            
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


def Summarize_results(embedding_method):
    result_filename = "RESULTS_COBYLA_"+embedding_method.name
    imp = __import__(result_filename)
    R = imp.RESULTS
    
    fname = "RESULTS_COBYLA_"+embedding_method.name+"_summary.txt"
    output_file = open(fname, 'w+')
    for i in range(len(R)):
        
        fopt = [ R[i][j].f_opt for j in range(len(R[i]))]
        fevals = [ R[i][j].fevals for j in range(len(R[i]))]
        times = [ R[i][j].time for j in range(len(R[i]))]
        
        print >>output_file, ""
        print >>output_file, "Sim budget =",simulation_budget[i],"simulation length = ", embedding_method.get_simulation_length(simulation_budget[i]),
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

#Select the embedding method:
embedding_method = OptimizationProblem.Embedding_randomization()

#Run optimization
Run_COBYLA(embedding_method)
Summarize_results(embedding_method)


