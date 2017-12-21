#OptimizationProblem.py
#Define the objective function, bounds, number of trials etc.


import os,sys

sys.path.insert(0, '../../0_Model')
from SimulationWrapper_System_3_servers import *



class OptimizationProblem:
    
    #static members
    NUM_DIMENSIONS=7
    param_min_value=1.0 #min bound
    param_max_value=10.0 #max bound

    def __init__(self):
        
        #default values for simulation parameters
        self.W = 1.0  # weight assigned to cost component
        self.sim_length=10000 #simulation length
        self.rand_seed=1 #randomization seed for the simulation
        
        #default values for other (fixed) system parameters
        self.p=0.5
        self.q2=0.1
        self.K1=1
        self.alpha=0.5
        
        #bounds
        self.bounds=[]
        for i in range(self.NUM_DIMENSIONS):
            self.bounds.append([self.param_min_value, self.param_max_value])

        #constraints
        self.constraints=[(lambda x,i=i: x[i]-self.param_min_value) for i in range(self.NUM_DIMENSIONS)]
        self.constraints.extend([(lambda x,i=i: self.param_max_value- x[i]) for i in range(self.NUM_DIMENSIONS)])

        # variable to keep track of the
        # number of times the objective function is called.
        self.objective_function_count=0
        
        #compute the maximum cost
        self.X_max_cost = [10,10,10,1,1,10,10]
        self.max_cost=self.Cost(self.X_max_cost)



    def Simulation(self,x) :
        #variables:
        C1=x[0]
	C2=x[1]
	C3=x[2]

	T1=x[3]
	T3=x[4]
	
        K2=x[5]
	K3=x[6]

        #beta
        beta = 1.0/T3

        #run simulation:
        blocking_probability, average_num_jobs_in_system, average_throughput = \
        run_simulation(self.rand_seed, self.sim_length, self.p, C1,C2,C3,T1,self.q2,T3,self.K1,K2,K3,self.alpha,beta)
	
        return blocking_probability, average_num_jobs_in_system, average_throughput

    
    def NormalizedThroughput(self,x):
        blocking_probability, average_num_jobs_in_system, average_throughput = self.Simulation(x)
        max_throughput=self.p
        return average_throughput/max_throughput
        

    #cost function
    def Cost(self,x) :
            C1=float(x[0])
            C2=float(x[1])
            C3=float(x[2])

            T1=float(x[3])
            T3=float(x[4])
            
            K2=float(x[5])
            K3=float(x[6])

            cost  = 5.0*(C1+C2+C3)
            cost += 100.0 * (1.0/T1)
            cost += 500.0 * K2
            cost += 100.0 * K3/T3
            return cost
    
    def NormalizedCost(self,x):
        return self.Cost(x)/self.max_cost

    def Clip(self,x):
        y=[]
        #clip all parameter values to lie in the interval [1,10] 
        #and convert to float
        for i in range(len(x)):
            y.append(min(self.param_max_value, (max(self.param_min_value, float(x[i]))) ))
        return y
  
    def Round(self,x):
        y=[]
        #round the vector x to the nearest integer point
        for i in range(len(x)):
            y.append(int(round(float(x[i]))))
        return y



    def ObjectiveFunction(self,x) :
            
            self.objective_function_count += 1

            #clip all parameter values to lie in the interval [1,10] 
            #and convert to float
            x = self.Clip(x)

            throughput=self.NormalizedThroughput(x)
            cost= self.NormalizedCost(x)

            #Objective to be minimized:
            objective_value = self.W* cost - throughput
            #print "x=",x,"f(x)=",objective_value,"W=",self.W,"Norm Throughput = ", throughput,"Norm Cost = ",cost
            return objective_value


#Test:
#OP=OptimizationProblem()
#OP.ObjectiveFunction([1,1,1,10,10,1,1])
#OP.ObjectiveFunction([5,5,5,5,5,5,5])
#OP.ObjectiveFunction([10,10,10,1,1,10,10])
