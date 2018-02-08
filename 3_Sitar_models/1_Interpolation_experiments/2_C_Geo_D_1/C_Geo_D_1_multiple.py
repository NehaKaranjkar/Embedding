import matplotlib.pyplot as plt
import numpy as np
import math
import os, sys

sys.path.insert(0, '../../0_Model')
import SimulationWrapper_SingleServer
import time

#create arrays
min_y=1
max_y=4
num_y=(max_y-min_y)*10+1

#Sweep C
y=np.linspace(min_y,max_y,num_y)

#fixed values:
sim_length=10000
p=0.49
T=2
K=1
NUM_RUNS=100

stencil_size=2


def sweep(r,s):
    fy_mean=[]
    fy_std_dev=[]
    computational_time=[]
    
    for i in range(len(y)):
        C=float(y[i])
        fy_values=[]
        start_time=time.time()
        for j in range(NUM_RUNS):
            rand_seed = 42+j
            pb, avg_num, throughput = SimulationWrapper_SingleServer.run_simulation_with_deterministic_servers( rand_seed, sim_length, p, C, T, K, stencil_size, r, s)
            fy_values.append(pb)
        
        end_time=time.time()
        computational_time.append((end_time-start_time)/float(NUM_RUNS))
        fy_mean.append(np.mean(fy_values))
        fy_std_dev.append(np.std(fy_values,ddof=1))
    #discrete points
    yd =[]
    fyd=[]
    for i in range(len(y)) :
        if(y[i].is_integer()):
            yd.append(y[i])
            fyd.append(fy_mean[i])
    #+- n-sigma interval around the mean
    n=3
    y1 = [fy_mean[i]-n*fy_std_dev[i] for i in range(len(y))]
    y2=  [fy_mean[i]+n*fy_std_dev[i] for i in range(len(y))]
    return fy_mean, fy_std_dev, computational_time, yd, fyd, y1,y2



#plot     
from matplotlib import pyplot as plt

def plot():
    
    # Three subplots sharing both x/y axes
    f, ((ax1, ax2, ax3), (ax4, ax5,ax6)) = plt.subplots(2,3, sharex=True, sharey=True)

    # r=1,s=1
    r =1
    s =1

    fy_mean, fy_std_dev, computational_time, yd, fyd, y1,y2 = sweep(r=r,s=s)
    ax1.scatter(y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    ax1.scatter(yd,fyd, s=60, c='yellow', alpha=1, label=r"Mean $f(y)$"+"(original model)")
    ax1.set_xlim([min_y-0.5,max_y+0.5])
    ax1.set_yticks([0.0,0.1,0.2])
    ax1.set_xticks([v for v in yd])
    ax1.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm\ 3\sigma$ interval")
    ax1.text(2.0,0.16,r"$r="+str(r)+",s="+str(s)+"$",fontsize=17)
    ax1.grid()
    
    r =1
    s =-1
    fy_mean, fy_std_dev, computational_time, yd, fyd, y1,y2 = sweep(r=r,s=s)
    ax2.scatter(y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    ax2.scatter(yd,fyd, s=60, c='yellow', alpha=1, label=r"Mean $f(y)$"+"(original model)")
    ax2.set_yticks([0.0,0.1,0.2])
    ax2.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm\ 3\sigma$ interval")
    ax2.text(2.0,0.16,r"$r="+str(r)+",s="+str(s)+"$",fontsize=17)
    ax2.grid()
  
    r =1
    s =-2
    fy_mean, fy_std_dev, computational_time, yd, fyd, y1,y2 = sweep(r=r,s=s)
    ax3.scatter(y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    ax3.scatter(yd,fyd, s=60, c='yellow', alpha=1, label=r"Mean $f(y)$"+"(original model)")
    ax3.set_yticks([0.0,0.1,0.2])
    ax3.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm\ 3\sigma$ interval")
    ax3.text(2.0,0.16,r"$r="+str(r)+",s="+str(s)+"$",fontsize=17)
    ax3.grid()

    r =1
    s =-4
    fy_mean, fy_std_dev, computational_time, yd, fyd, y1,y2 = sweep(r=r,s=s)
    ax4.scatter(y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    ax4.scatter(yd,fyd, s=60, c='yellow', alpha=1, label=r"Mean $f(y)$"+"(original model)")
    ax4.set_yticks([0.0,0.1,0.2])
    ax4.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm\ 3\sigma$ interval")
    ax4.text(2.0,0.16,r"$r="+str(r)+",s="+str(s)+"$",fontsize=17)
    ax4.grid()
    
    r = 2
    s =-2
    fy_mean, fy_std_dev, computational_time, yd, fyd, y1,y2 = sweep(r=r,s=s)
    ax5.scatter(y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    ax5.scatter(yd,fyd, s=60, c='yellow', alpha=1, label=r"Mean $f(y)$"+"(original model)")
    ax5.set_yticks([0.0,0.1,0.2])
    ax5.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm\ 3\sigma$ interval")
    ax5.text(2.0,0.16,r"$r="+str(r)+",s="+str(s)+"$",fontsize=17)
    ax5.grid()

    r = 0.5
    s =-2
    fy_mean, fy_std_dev, computational_time, yd, fyd, y1,y2 = sweep(r=r,s=s)
    ax6.scatter(y, fy_mean, s=10, c='black', alpha=0.5, label=r"Mean $\hat{f}(y)$"+"(randomized model)")
    ax6.scatter(yd,fyd, s=60, c='yellow', alpha=1, label=r"Mean $f(y)$"+"(original model)")
    ax6.set_yticks([0.0,0.1,0.2])
    ax6.fill_between(y,y1,y2, alpha=0.1, edgecolor='b',facecolor='b',label=r"$\pm\ 3\sigma$ interval")
    ax6.text(2.0,0.16,r"$r="+str(r)+",s="+str(s)+"$",fontsize=17)
    ax6.grid()


   # Fine-tune figure; make subplots close to each other and hide x ticks for
   # all but bottom plot.
    f.subplots_adjust(hspace=0.05, wspace=0.05)
    plt.setp([a.get_xticklabels() for a in [ax1,ax2]], visible=False)
    ax1.legend().draggable()
    f.text(0.5, 0.04, "Queue capacity "+r"$y$", ha='center')
    f.text(0.04, 0.5, "Blocking Probability "+r"$f(y)$", va='center', rotation='vertical')
    #plt.savefig("GD1_C_multiple.pdf")
    plt.show()


plot()

