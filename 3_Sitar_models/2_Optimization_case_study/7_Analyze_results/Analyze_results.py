# Analyze results of optimization

import os,sys
import numpy as np

from operator import attrgetter
from collections import namedtuple

import RESULTS_COBYLA as R
from tabulate import tabulate


def PrintSolutions():

    for i in range(len(R.RESULTS)):
        print "=================================="
        #sort results for simulation length=i
        #in ascending order of f_opt
        sorted_results = sorted(R.RESULTS[i], key=attrgetter('f_opt'))
        filtered_results=sorted_results[:20]

        #print as a table
        param_names = ["C1","C2","C3","T1","T3","K2","K3"]
        print tabulate([filtered_results[i][0] for i in range (len(filtered_results))],param_names)

        for l in range(len(filtered_results)):
            c1=filtered_results[l][0][0]
            c2=filtered_results[l][0][1]
            c3=filtered_results[l][0][2]
            k3=filtered_results[l][0][6]
            
            C = (2*k3) + (c1+c2+c3)
            T = filtered_results[l][2]

            #print "C=",C,"T=",T,"sum=",C+T

        #make a scatter plot for pairs of columns
        
        #columns to plot:
        x = 1
        y = 6
        X = [filtered_results[i][0][x] for i in range (len(filtered_results))]
        Y = [filtered_results[i][0][y] for i in range (len(filtered_results))]

        import matplotlib.pyplot as plt
        import math
        import matplotlib
        cmap = matplotlib.cm.get_cmap('Spectral')
	fig=plt.figure();
        plt.scatter(X,Y, marker='o', s=50, alpha=0.3)
	plt.xlabel(param_names[x])
	plt.ylabel(param_names[y])
	plt.grid()
	#plt.show()





PrintSolutions()



