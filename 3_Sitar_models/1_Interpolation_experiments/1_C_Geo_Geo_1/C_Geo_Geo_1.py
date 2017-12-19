import matplotlib.pyplot as plt
import numpy as np
import math
import os, sys
import time

sys.path.insert(0, '../../0_Model')
import SimulationWrapper_SingleServer

#sweep parameter y
min_y=1
max_y=5
num_y=(max_y-min_y)*20+1
y=np.linspace(min_y,max_y,num_y)

#results:
fy_mean=[]
fy_std_dev=[]
computational_time=[]

#simulation settings:
sim_length=10000
p=0.5
q=0.51
K=1
NUM_RUNS=100

#randomization settings
stencil_size=2
r=1.0
s=-1.0

def sweep():
    for i in range(len(y)):
        C=float(y[i])
        fy_values=[]
        start_time=time.time()
        for j in range(NUM_RUNS):
            rand_seed = 42+j
            pb, avg_num, throughput = SimulationWrapper_SingleServer.run_simulation_with_geom_servers( rand_seed, sim_length, p, C, q, K, stencil_size, r, s)
            fy_values.append(pb)
        
        end_time=time.time()
        computational_time.append((end_time-start_time)/float(NUM_RUNS))
        fy_mean.append(np.mean(fy_values))
        fy_std_dev.append(np.std(fy_values,ddof=1))

#plot     
from matplotlib import pyplot as plt

def plot():
    
    fig1=plt.figure();
    
    from pylab import rcParams
    rcParams['figure.figsize'] = 4, 6
 
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
    n=3
    y1 = [fy_mean[i]-n*fy_std_dev[i] for i in range(len(y))]
    y2=  [fy_mean[i]+n*fy_std_dev[i] for i in range(len(y))]

    plt.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm 3 \sigma$ interval")
    plt.legend().draggable()

    #plt.title("Simulation length = 500000 jobs\n")
    plt.xlabel("Queue capacity "+r"$y$")
    plt.ylabel("Blocking Probability "+r"$f(y)$")
    plt.grid()
    plt.savefig("fig.pdf")
    plt.show()



sweep()
plot()

