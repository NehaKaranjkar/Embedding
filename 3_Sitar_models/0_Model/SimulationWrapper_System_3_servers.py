#Wrapper to call C++ function from python.
import ctypes
import os

script_file=os.path.realpath(__file__)
script_path=os.path.dirname(script_file)
sitar_lib_path=script_path+"/lib/libSystem_3_servers.so"
sitar_sim = ctypes.CDLL(sitar_lib_path)


sitar_sim.run_simulation.argtypes = (  
ctypes.c_int,	                    #int rand_seed,//randomization seed                           	
ctypes.c_ulong, 	            #uint64_t simulation_length,//simulation length in cycles           
ctypes.c_double,	            #double p, //job arrival probability
ctypes.c_double,	            #double C1,//queue capacity at the input of server 1
ctypes.c_double,	            #double C2,//queue capacity at the input of server 2
ctypes.c_double,	            #double C3,//queue capacity at the input of server 3 
ctypes.c_double,	            #double T1,//service delay of server 1 (deterministic)
ctypes.c_double,	            #double q2,//service probability of server 2 (geom)
ctypes.c_double,	            #double T3,//service delay of server 3 (deterministic)
ctypes.c_double,	            #double K1,//number of service nodes in server 1                  
ctypes.c_double,	            #double K2,//number of service nodes in server 2                  
ctypes.c_double,	            #double K3,//number of service nodes in server 3                  
ctypes.c_double,	            #double alpha, //probability that output of s1 goes to s2.
ctypes.c_double,	            #double beta,  //probability that output of s3 goes back to s1
ctypes.POINTER(ctypes.c_double),    #double* blocking_probability,                                      
ctypes.POINTER(ctypes.c_double),    #double* average_num_jobs_in_system,                                
ctypes.POINTER(ctypes.c_double))    #double* average_throughput)

def run_simulation(rand_seed, simulation_length, p, C1,C2,C3,T1,q2,T3,K1,K2,K3,alpha,beta):
    global sitar_sim
    blocking_probability       = ctypes.c_double()
    average_num_jobs_in_system = ctypes.c_double()
    average_throughput         = ctypes.c_double()
    
    sitar_sim.run_simulation(rand_seed, simulation_length, p,C1,C2,C3,T1,q2,T3,K1,K2,K3,alpha,beta, ctypes.byref(blocking_probability), ctypes.byref(average_num_jobs_in_system), ctypes.byref(average_throughput))
    return blocking_probability.value, average_num_jobs_in_system.value, average_throughput.value

#Test for this wrapper
def TestCase():
    blocking_probability       = 0.0
    average_num_jobs_in_system = 0.0
    average_throughput         = 0.0
    rand_seed=1
    simulation_length=10000
    p=0.1
    C1=2
    C2=2
    C3=2
    T1=5
    q2=0.5
    T3=5
    K1=1
    K2=1
    K3=1
    alpha=0.5
    beta=0.5
    blocking_probability, average_num_jobs_in_system, average_throughput = run_simulation(rand_seed, simulation_length, p, C1,C2,C3,T1,q2,T3,K1,K2,K3,alpha,beta)
    print " Result : ", blocking_probability," ", average_num_jobs_in_system, " ", average_throughput

#TestCase()
