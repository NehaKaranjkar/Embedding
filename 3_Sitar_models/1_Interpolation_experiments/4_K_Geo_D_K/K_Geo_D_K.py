import matplotlib.pyplot as plt
import numpy as np
import math
import os, sys
sys.path.insert(0, '../../0_Model')
import SimulationWrapper_SingleServer
import time

#create arrays
min_y=1.0
max_y=3.0

smallest_step=0.00005
largest_step=0.05

#generate y, such that step-size increases geometrically
y=[min_y]
v=min_y
step=smallest_step
while(v <= max_y):
    v = v + step
    y.append(v)
    step = step*1.5
    if(step > largest_step):
        step=largest_step

def sortAndUniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  output.sort()
  return output

y.extend([float(x) for x in range(int(min_y), int(max_y+1))])
y = sortAndUniq(y)
print y
print "y length=",len(y)
#plt.plot(y)
#plt.show()


fy_mean=[]
fy_std_dev=[]
computational_time=[]

#fixed values:
sim_length=10000
p=0.49
T=2.0
C=0 #infinite buffering
NUM_RUNS=100

#Randomization generator functions
h_function_C=1  #use h(y)=1/y
h_function_K=0  #use h(y)=y
h_function_T=0  #use h(y)=y

def sweep():
    for i in range(len(y)):
        K=float(y[i])
        fy_values=[]
        start_time=time.time()
        for j in range(NUM_RUNS):
            rand_seed = 42+j
            pb, avg_num, throughput = SimulationWrapper_SingleServer.run_simulation_with_deterministic_servers( rand_seed, sim_length, p, C, T, K, h_function_C, h_function_K, h_function_T)
            fy_values.append(avg_num)
        
        end_time=time.time()
        computational_time.append((end_time-start_time)/float(NUM_RUNS))
        fy_mean.append(np.mean(fy_values))
        fy_std_dev.append(np.std(fy_values,ddof=1))

#plot     
from matplotlib import pyplot as plt

def plot():
    
    fig1=plt.figure();
 
    #plot mean 
    plt.scatter(y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    #plot discrete points
    yd =[]
    fyd=[]
    for i in range(len(y)) :
            if(y[i].is_integer()):
                    yd.append(y[i])
                    fyd.append(fy_mean[i])
    plt.scatter(yd,fyd, s=60, c='yellow', alpha=1, label=r"Mean $f(y)$"+"(original model)")
    plt.xlim([min_y-0.5,max_y+0.5])
    plt.ylim([-1.2,17.5])
    plt.xticks([x for x in range(int(min_y),int(max_y)+1)])
       
    #plot computation time
    #plt.plot(y,[(x*1000) for x in computational_time],'k-', label="Avg computational time per simulation (in ms)")
    time_min=min(computational_time)
    time_max=max(computational_time)
    computational_overhead=(time_max-time_min)/time_min
    print "Computational overhead of randomization:";
    print "Max time=", time_max
    print "Min time=", time_min
    print "Overhead = ",computational_overhead*100,"%"
    
    #plot +-n sigma interval around the mean
    n=1
    y1 = [fy_mean[i]-n*fy_std_dev[i] for i in range(len(y))]
    y2=  [fy_mean[i]+n*fy_std_dev[i] for i in range(len(y))]

    plt.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm 1 \sigma$ interval")
    plt.legend().draggable()

    plt.xlabel("Number of servers "+r"$y$")
    plt.ylabel("Average number of jobs in system "+r"$f(y)$")
    plt.grid()
    plt.show()


sweep()
print "y=",y
plot()

