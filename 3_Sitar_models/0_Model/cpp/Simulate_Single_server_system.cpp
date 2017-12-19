//Simulate_Single_server_system.cpp

#include"System_Geom_D.h"
#include"System_Geom_Geom.h"
#include"sitar_simulation.h"
#include"sitar_logger.h"
#include<cstdlib>
#include<iostream>
#include<cassert>
#include<stdint.h>
#include<math.h>
#include<map>
#include"RandomGenerator.h"
#include"PerturbedParameter.h"

using namespace std;
using namespace sitar;


//random number generator:
RandomGenerator* randomGenerator;


extern "C" {

//Simulation of a Queue with
// Poisson arrivals (probability of arrival in a cycle=p)
// Deterministic server
// 	T: service time (default =1)
// 	K: number of servers (default=1)
// 	C: bufferig at the server (0 implies infinite buffering)
//simulation_length : total simulation length in cycles.
void run_simulation_with_deterministic_servers(\
		int rand_seed,
		uint64_t simulation_length, 
		double p, 
		double C, 
		double T,
		double K,
		int stencil_size,
		double r,
		double s,
		double* blocking_probability,
		double* average_num_jobs_in_system,
		double* average_throughput)
{
	
	//do elaboration
	System_Geom_D TOP;
	TOP.setInstanceId("TOP");
	TOP.setHierarchicalId("");

	//make a random generator and seed it
	randomGenerator = new RandomGenerator;
	randomGenerator->seedRandomEngine(rand_seed);

	//set simulation parameters
	TOP.source.p=p;
	TOP.server.C=C;
	TOP.server.T=T;
	TOP.server.K=K;

	//set randomization settings:
	//(same for all parameters)
	TOP.server.C_value.initialize(stencil_size, r, s, C);
	TOP.server.T_value.initialize(stencil_size, r, s, T);
	TOP.server.K_value.initialize(stencil_size, r, s, K);

	sitar::restart_simulation();
	
	uint64_t i;

	double current_occupancy=0;
	double avg_occupancy=0;

	for(i=0; i<simulation_length ;i++)
	{
		//phase 0
		TOP.run(i<<1);
		
		//phase 1
		TOP.run(i<<1 | 1);

		//update average occupancy metric
		current_occupancy = TOP.server.Q.size + TOP.server.ongoing_jobs;
		avg_occupancy = avg_occupancy*i/(i+1) + current_occupancy/(i+1);

		if(sitar::simulation_stopped()) break;
	};
	//compute performance metrics
	assert(i);
	assert(TOP.source.jobs_generated);
	
	*blocking_probability = ((double)TOP.source.jobs_lost)/((double)(TOP.source.jobs_generated));
	*average_num_jobs_in_system = avg_occupancy;
	*average_throughput = ((double)TOP.server.jobs_served)/((double)(i)) ;
	return;
}

//Simulation of a Queue with
// Poisson arrivals (probability of arrival in a cycle=p)
// Geometric service times
// 	q: Probability that the server finishes an ongoing job in current slot
// 	K: number of servers (default=1)
// 	C: bufferig at the server (0 implies infinite buffering)
//simulation_length : total simulation length in cycles.
void run_simulation_with_geom_servers(\
		int rand_seed,
		uint64_t simulation_length, 
		double p, 
		double C, 
		double q,
		double K,
		int stencil_size,
		double r,
		double s,
		double* blocking_probability,
		double* average_num_jobs_in_system,
		double* average_throughput)
{
	
	//do elaboration
	System_Geom_Geom TOP;
	TOP.setInstanceId("TOP");
	TOP.setHierarchicalId("");

	//make a random generator and seed it
	randomGenerator = new RandomGenerator;
	randomGenerator->seedRandomEngine(rand_seed);

	//set simulation parameters
	TOP.source.p=p;
	TOP.server.C=C;
	TOP.server.q=q;
	TOP.server.K=K;
	
	//set interpolation functions for each of these parameters
	TOP.server.C_value.initialize(stencil_size,r,s,C);
	TOP.server.K_value.initialize(stencil_size,r,s,K);
	
	sitar::restart_simulation();
	
	uint64_t i;

	double current_occupancy=0;
	double avg_occupancy=0;

	for(i=0; i<simulation_length ;i++)
	{
		//phase 0
		TOP.run(i<<1);
		
		//phase 1
		TOP.run(i<<1 | 1);

		//update average occupancy metric
		current_occupancy = TOP.server.Q.size + TOP.server.ongoing_jobs;
		avg_occupancy = avg_occupancy*i/(i+1) + current_occupancy/(i+1);

		if(sitar::simulation_stopped()) break;
	};
	//compute performance metrics
	assert(i);
	assert(TOP.source.jobs_generated);
	
	*blocking_probability = ((double)TOP.source.jobs_lost)/((double)(TOP.source.jobs_generated));
	*average_num_jobs_in_system = avg_occupancy;
	*average_throughput = ((double)TOP.server.jobs_served)/((double)(i)) ;
	return;
}

}

//Just for testing:
int main()
{
	double blocking_probability=0;
	double average_num_jobs_in_system=0;
	double average_throughput=0;

	run_simulation_with_deterministic_servers(\
	42, //rand seed		
	100000,//uint64_t simulation_length, 
	0.9, //	double p, 
	5.5, //	double C, 
	2.2, //	double T,
	1.9, //	double K,
	2, //stencil_size 
	1.0, //r
	1.0, //s
	&blocking_probability, //	double* blocking_probability,
	&average_num_jobs_in_system, //	double* average_num_jobs_in_system,
	&average_throughput);	//	double* average_throughput)
	std::cout<<"\n\n Geom_D server";
	std::cout<<"\n blocking_probability = "<<blocking_probability;
	std::cout<<"\n average_num_jobs_in_system = "<<average_num_jobs_in_system;
	std::cout<<"\n average_throughput = "<<average_throughput;
	
	run_simulation_with_geom_servers(\
	42, //rand seed		
	100000,//uint64_t simulation_length, 
	0.9, //	double p, 
	5.5, //	double C, 
	0.4, //	double q,
	1.9, //	double K,
	2, //stencil_size
	1.0, //r
	1.0, //s
	&blocking_probability, //	double* blocking_probability,
	&average_num_jobs_in_system, //	double* average_num_jobs_in_system,
	&average_throughput);	//	double* average_throughput)

	std::cout<<"\n\n Geom_Geom server";
	std::cout<<"\n blocking_probability = "<<blocking_probability;
	std::cout<<"\n average_num_jobs_in_system = "<<average_num_jobs_in_system;
	std::cout<<"\n average_throughput = "<<average_throughput;


	return 0;
}



