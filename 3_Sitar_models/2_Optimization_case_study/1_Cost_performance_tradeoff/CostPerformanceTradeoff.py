#Cost Performance Analysis



import random
import sys, os


#Create an instance of the optimization problem
sys.path.insert(0, '../0_Optimization_problem')
import OptimizationProblem

OP = OptimizationProblem.OptimizationProblem()
OP.sim_length=100000
OP.rand_seed=42


#some randomly chosen initial guesses for optimization:
initial_guesses = []
NUM_TRIALS=10


for i in range(NUM_TRIALS):
    initial_guesses.append([])
    for j in range(OP.NUM_DIMENSIONS):
        initial_guesses[i].append(random.randint(OP.bounds[j][0],OP.bounds[j][1]))

print "Initial guesses: ",initial_guesses


import numpy
from scipy.optimize import fmin_cobyla
	

#sweep the cost-weight W to get a cost-performance curve
weights=[0, 0.25, 0.5, 1, 2.5, 5.0, 7.5, 10]
print "Weights=",weights


def getCostPerformanceCurve():
	X_opt=[]
	f_opt=[]
	TP_opt=[]
	cost_opt=[]

	for i in range(len(weights)) :
		OP.W = weights[i]
		X_opt.append([])
		TP_opt.append([])
		cost_opt.append([])
		f_opt.append([])
		
		for j in initial_guesses:
			x = fmin_cobyla(func=OP.ObjectiveFunction, 
				x0=j,
				cons=OP.constraints,
				rhobeg=1,
				rhoend=1e-3)

			X_opt[i].append(x)
			TP_opt[i].append(OP.NormalizedThroughput(OP.Clip(x)))
			cost_opt[i].append(OP.NormalizedCost(OP.Clip(x)))
			f_opt[i].append(OP.ObjectiveFunction(x))
	
	#write the arrays out to a file
	with open("RESULT_X_opt.py", "w") as f:
		print >>f, "X_opt=",X_opt
	with open("RESULT_TP_opt.py", "w") as f:
		print >>f, "TP_opt=",TP_opt
	with open("RESULT_cost_opt.py", "w") as f:
		print >>f, "cost_opt=",cost_opt
	with open("RESULT_f_opt.py", "w") as f:
		print >>f, "f_opt=",f_opt

#plot cost-performance
import matplotlib.pyplot as plt
import math
import matplotlib
cmap = matplotlib.cm.get_cmap('Spectral')



def PlotCostPerformanceCurve():
	import RESULT_TP_opt, RESULT_cost_opt
	fig1=plt.figure();
	
        for i in range(len(weights)) :
		X =RESULT_cost_opt.cost_opt[i]
		Y =RESULT_TP_opt.TP_opt[i]
		plt.scatter(X,Y, marker='o', color = cmap(float(i)/(len(weights)-1)), s=50, alpha=0.7, label=r"$W=$"+str(weights[i]))

	plt.title("Throughput versus Cost obtained by sweeping cost-weight W\n")
	plt.xlabel("Normalized Cost")
	plt.ylabel("Normalized Throughput")
	plt.grid()
	plt.legend().draggable()
	plt.show()

getCostPerformanceCurve()
PlotCostPerformanceCurve()

