# Analyze results of optimization using COBYLA

import os,sys
import numpy as np

from operator import attrgetter
from collections import namedtuple
from Optimize_COBYLA import *

import RESULTS as R

def PrintSummary():
    
    for i in range(len(R.RESULTS)):
        print "================================="
        print "Sim length=",simulation_lengths[i],
        f = [R.RESULTS[i][j].f_opt for j in range(len(R.RESULTS[i]))]
        print "\n\t f_avg=",np.mean(f),
        print "\t f_stdd=",np.std(f,ddof=1),
        print "\t f_best=",np.min(f),
        print "\t f_worst=",np.max(f),
        fevals = [R.RESULTS[i][j].fevals for j in range(len(R.RESULTS[i]))]
        print "\n\t fevals_avg=",np.mean(fevals),
        print "\t fevals_stdd=",np.std(fevals,ddof=1),
        print "\t fevals_best=",np.min(fevals),
        print "\t fevals_worst=",np.max(fevals),
        opt_time = [R.RESULTS[i][j].time for j in range(len(R.RESULTS[i]))]
        print "\n\t time_avg=",np.mean(opt_time),
        print "\t time_stdd=",np.std(opt_time,ddof=1),
        print "\t time_best=",np.min(opt_time),
        print "\t time_worst=",np.max(opt_time),

def PrintSolutions():

    for i in range(len(R.RESULTS)):
        print "=================================="
        print "Sim length=",simulation_lengths[i]
        
        #sort results for simulation length=i
        #in ascending order of f_opt
        sorted_results = sorted(R.RESULTS[i], key=attrgetter('f_opt'))
        sorted_f       = [sorted_results[j].f_opt for j in range(len(sorted_results))]
        sorted_x       = [sorted_results[j].x_opt for j in range(len(sorted_results))]

        for j in range(len(sorted_x)):
            print "f_opt=",sorted_f[j],"\t x=",sorted_x[j]

PrintSummary()
PrintSolutions()



