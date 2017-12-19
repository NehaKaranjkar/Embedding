#Wrapper to call C++ function from python.
import ctypes
import os

script_file=os.path.realpath(__file__)
script_path=os.path.dirname(script_file)
sitar_lib_path=script_path+"/lib/libSingleServer.so"

sitar_sim = ctypes.CDLL(sitar_lib_path)
sitar_sim.run_simulation_with_deterministic_servers.argtypes = (  
ctypes.c_int,		#int rand_seed,
ctypes.c_ulong, 	#uint64_t simulation_length, 
ctypes.c_double,	#double p, 
ctypes.c_double,	#double C, 
ctypes.c_double,	#double T,
ctypes.c_double,	#double K,
ctypes.c_int,	        #int stencil_size
ctypes.c_double,        #double r
ctypes.c_double,        #double s
ctypes.POINTER(ctypes.c_double),	#double* blocking_probability,
ctypes.POINTER(ctypes.c_double),	#double* average_num_jobs_in_system,
ctypes.POINTER(ctypes.c_double))	#double* average_throughput)

sitar_sim.run_simulation_with_geom_servers.argtypes = (  
ctypes.c_int,		#int rand_seed,
ctypes.c_ulong, 	#uint64_t simulation_length, 
ctypes.c_double,	#double p, 
ctypes.c_double,	#double C, 
ctypes.c_double,	#double q,
ctypes.c_double,	#double K,
ctypes.c_int,	        #int stencil_size
ctypes.c_double,        #double r
ctypes.c_double,        #double s
ctypes.POINTER(ctypes.c_double),	#double* blocking_probability,
ctypes.POINTER(ctypes.c_double),	#double* average_num_jobs_in_system,
ctypes.POINTER(ctypes.c_double))	#double* average_throughput)



def run_simulation_with_deterministic_servers( rand_seed, simulation_length, p, C, T, K, stencil_size,r ,s):
    global sitar_sim
    blocking_probability       = ctypes.c_double()
    average_num_jobs_in_system = ctypes.c_double()
    average_throughput         = ctypes.c_double()
    
    sitar_sim.run_simulation_with_deterministic_servers(rand_seed, simulation_length, p,C,T,K, stencil_size,r,s, ctypes.byref(blocking_probability), ctypes.byref(average_num_jobs_in_system), ctypes.byref(average_throughput))
    return blocking_probability.value, average_num_jobs_in_system.value, average_throughput.value

def run_simulation_with_geom_servers( rand_seed, simulation_length, p, C, q, K, stencil_size, r, s):
    global sitar_sim
    blocking_probability       = ctypes.c_double()
    average_num_jobs_in_system = ctypes.c_double()
    average_throughput         = ctypes.c_double()
    
    sitar_sim.run_simulation_with_geom_servers(rand_seed, simulation_length, p,C,q,K,stencil_size, r, s, ctypes.byref(blocking_probability), ctypes.byref(average_num_jobs_in_system), ctypes.byref(average_throughput))
    return blocking_probability.value, average_num_jobs_in_system.value, average_throughput.value



#Test for this wrapper
def TestCase():
    blocking_probability       = 0.0
    average_num_jobs_in_system = 0.0
    average_throughput         = 0.0
    rand_seed=1
    simulation_length=10000
    stencil_size = 2
    r = 1.0
    s = 1.0
    p=0.5
    C=1
    q=0.6
    K=1
    blocking_probability,average_num_jobs_in_system, average_throughput= run_simulation_with_geom_servers(rand_seed, simulation_length, p,C,q,K,stencil_size, r, s)
    print " Result : ", blocking_probability," ", average_num_jobs_in_system, " ", average_throughput

TestCase()
