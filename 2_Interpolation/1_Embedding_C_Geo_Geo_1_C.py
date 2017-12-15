# Embedding queue capacity C
# in a Geo/Geo/1/C queue

import random
import simpy

from Job import Job
from Buffer import EmbeddedBuffer
from Source_Geo import Source_Geo
from Server_Geo import Server_Geo
from Gamma import *
from Alphas import *

#bounds on parameter values
y_min_bound = 1
y_max_bound = 5

#randomization settings:
stencil_size=2
s=1
r=1

#Fixed parameters
arrival_probability=0.5
service_probability=0.51
simulation_length = 1e1

#Parameter sweep settings:
num_y=(y_max_bound-y_min_bound)*20+1
Y=np.linspace(y_min_bound, y_max_bound,num_y)
number_of_simulations_per_point=10


def Simulate(y, rand_seed, simulation_length):
        
    env=simpy.Environment()
    random.seed(rand_seed) 
    
    stencil, alphas= get_stencil_and_alphas(y,y_min_bound,y_max_bound,stencil_size,s,r)
    gamma = Gamma(stencil,alphas)
    C = EmbeddedBuffer(env,gamma)
    Source = Source_Geo(env,"Source",arrival_probability,C)
    Server = Server_Geo(env,"Server",service_probability,C)
    env.run(until=simulation_length)

    average_length = C.average_length
    average_throughput = Server.average_throughput
    blocking_probability = Source.blocking_probability

    return average_length,average_throughput,blocking_probability


import os, sys
import time


#results:
fy_mean=[]
fy_std_dev=[]
computational_time=[]


def Sweep_y():
    for i in range(len(Y)):
        y=Y[i]
        
        fy_values=[]
        
        #start timer
        start_time=time.time() 
        
        #perform multiple simulations
        #with distinct rand_seeds
        for j in range(number_of_simulations_per_point):
            rand_seed = 42+j
            average_length,average_throughput,blocking_probability = Simulate(y, rand_seed, simulation_length)
            fy_values.append(blocking_probability)

        #stop timer
        end_time=time.time()
        computational_time.append((end_time-start_time)/float(number_of_simulations_per_point))
        fy_mean.append(np.mean(fy_values))
        fy_std_dev.append(np.std(fy_values,ddof=1))




#plot     
from matplotlib import pyplot as plt

def Plot_interpolation():
    fig1=plt.figure();
 
    #plot mean 
    plt.scatter(Y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    #plot discrete points
    yd =[]
    fyd=[]
    for i in range(len(Y)) :
            if(is_int(Y[i])):
                    yd.append(int(Y[i]))
                    fyd.append(fy_mean[i])
    plt.scatter(yd,fyd, s=60, c='orange', edgecolor="black",alpha=1, label=r"Mean $f(y)$"+"(original model)")
    plt.xlim([y_min_bound-0.5,y_max_bound+0.5])
       
    #plot computation time
    #plt.plot(Y,[(x*1000) for x in computational_time],'k-', label="Avg computational time per simulation (in ms)")
    time_min=min(computational_time)
    time_max=max(computational_time)
    computational_overhead=(time_max-time_min)/time_min
    print("Computational overhead of randomization:");
    print("Max time=", time_max)
    print("Min time=", time_min)
    print("Overhead = ",computational_overhead*100,"%")
    
    #plot +-n sigma interval around the mean
    n=3
    y1 = [fy_mean[i]-n*fy_std_dev[i] for i in range(len(Y))]
    y2=  [fy_mean[i]+n*fy_std_dev[i] for i in range(len(Y))]

    plt.fill_between(Y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm 3 \sigma$ interval")
    plt.legend().draggable()

    #plt.title("Simulation length = 500000 jobs\n")
    plt.xlabel("Queue capacity "+r"$y$")
    plt.ylabel("Blocking Probability "+r"$f(y)$")
    plt.grid()
    plt.show()

Sweep_y()

#save results to a file
with open("1_Embedding_C_Geo_Geo_1_C.txt","w") as result_file:
    print("fy_mean=",fy_mean, file=result_file)
    print("fy_std_dev=",fy_std_dev, file=result_file)
    print("computational_time=",computational_time, file=result_file)


Plot_interpolation()

