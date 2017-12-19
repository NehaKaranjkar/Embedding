#Comput computational overhead of randomization

import os,sys
import numpy as np
import OptimizationProblem


#Create an instance of the optimization problem
OP = OptimizationProblem.OptimizationProblem()

OP.p=0.5
OP.q=0.1
OP.W = 1 #weight assigned to cost
OP.sim_length=1000000 #1e6
OP.rand_seed=42
NUM_DIMENSIONS=OP.NUM_DIMENSIONS


#param      #  0     1     2     3      4      5     6
param_names=["C_1","C_2","C_3", "T_1","T_3", "K_2", "K_3"]
param_min_value=1.0
param_max_value=10.0

#base point
x_base = [5,5,5,5,5,5,5]
x=x_base
avg_times=[]
for i in range(NUM_DIMENSIONS+1):
    
    
    print "x=",x,"Num parameters embedded = ",i,"Avg exec time=",avg_time, "Overhead=",overhead

    
#            Z[r][c] = OP.ObjectiveFunction(x)



