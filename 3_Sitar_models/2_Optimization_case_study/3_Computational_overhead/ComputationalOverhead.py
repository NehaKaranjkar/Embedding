# Find computational overhead of randomization

import os,sys
import numpy as np
import time

sys.path.insert(0, '../0_Optimization_problem')
import OptimizationProblem

#Create an instance of the optimization problem
OP = OptimizationProblem.OptimizationProblem()

#simulation parameters
OP.sim_length=1000000
OP.rand_seed=42
dimensions=OP.NUM_DIMENSIONS
runs_per_dimension = 10

#param      #  0     1     2     3      4      5     6
param_names=["C_1","C_2","C_3", "T_1","T_3", "K_2", "K_3"]
param_min_value=1.0
param_max_value=10.0

#This is the base point 
#relative to which 
#we compute the overhead
x_base =   [5,5,5,5,5,5,5]


def compute_overheads():
    
    avg_time_per_simulation=[0.0 for d in range(dimensions+1)]
    overheads=[0.0 for d in range(dimensions+1)]


    for n in range (dimensions+1):
        
        X = x_base[:]
        for i in range (n):
            X[i]+=0.5
        
        times =[]
        f_values=[]
        for run in range (runs_per_dimension):
            OP.rand_seed=run+42
            t_start = time.time()
            f_values.append(OP.ObjectiveFunction(X))
            t_end = time.time()
            times.append(t_end-t_start)

        avg_sim_time= np.mean(times)
        avg_time_per_simulation[n]= np.mean(times)

        t_base = avg_time_per_simulation[0]
        overhead= (float(avg_sim_time) - float(t_base))/float(t_base) * 100.0
        overheads.append(overhead)
        print "Num parameters embedded = ",n,"X=",X,"avg time per sim = ", avg_sim_time, "overhead = ", overhead," %"

compute_overheads()        



def sweep(param1, param2, min_val, max_val, step):

    X=np.arange(min_val, max_val+step, step)
    Y=np.arange(min_val, max_val+step, step)
    
    X,Y = np.meshgrid(X,Y)

    OP.objective_function_count=0
    
    rows=len(X)
    columns =len(X[0])
    runs = 100
    #Compute the result array Z
    Z = np.empty([rows,columns],dtype=float)

    print "Total points = ",rows*columns
    print "Simulations per point = ",runs
    print "Total simulations = ", runs*rows*columns 
    print "Simulation length = ",OP.sim_length

    for r in range(rows):
        for c in range(columns):
            x = x_base
            x[param1] = X[r][c]
            x[param2] = Y[r][c]
            z=[]
            
            t_start = time.time()
            #---------------------
            for run in range (runs):
                OP.rand_seed=run+42+r+c
                z.append(OP.ObjectiveFunction(x))
            Z[r][c] = np.mean(z)
            #---------------------
            t_end = time.time()

            if (OP.objective_function_count%100==0):
                print "#objective function calls = ",OP.objective_function_count,"avg time per call =",(t_end-t_start)/float(runs),"seconds"


    #store results in a file
    np.save("X_" + param_names[param1]+"_"+param_names[param2],X)
    np.save("Y_" + param_names[param1]+"_"+param_names[param2],Y)
    np.save("Z_" + param_names[param1]+"_"+param_names[param2],Z)

    return X, Y, Z



#Function to plot the contours
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotContours(param1,param2,fig_num=1):
	fig = plt.figure(fig_num)
	ax = Axes3D(fig)

	#load data from file:
        X = np.load("X_" + param_names[param1]+"_"+param_names[param2]+".npy")
        Y = np.load("Y_" + param_names[param1]+"_"+param_names[param2]+".npy")
        Z = np.load("Z_" + param_names[param1]+"_"+param_names[param2]+".npy")

	#ax.plot_wireframe(X, Y, Z,  cmap=plt.cm.Spectral,linewidth=1)
	ax.plot_surface(X, Y, Z, cstride=1, rstride=1, cmap=plt.cm.Spectral,linewidth=0.3,alpha=0.8)
	#cset = ax.contour(X, Y, Z, zdir='z', offset=-0.4,  cmap=plt.cm.coolwarm)
        
        ax.set_xlabel(param_names[param1])
        ax.set_ylabel(param_names[param2])
        ax.set_zlabel("f")
                
	plt.show()
	

# param      #  0     1     2     3      4      5     6
#param_names=["C_1","C_2","C_3", "T_1","T_3", "K_2", "K_3"]

#param1 = 1
#param2 = 2 
#sweep(param1,param2, min_val=1.0, max_val=10.0, step=0.25)
#plotContours(param1,param2,fig_num=1)


