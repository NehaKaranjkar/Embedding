//Simulate_System_3_servers.cpp

#include"System_3_servers.h"
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
#include"h_functions.h"

using namespace std;
using namespace sitar;


//random number generator:
RandomGenerator* randomGenerator;

extern "C" {

//Simulate the system with 3 servers
void run_simulation(\
		int rand_seed,//randomization seed
		uint64_t simulation_length,//simulation length in cycles 
		double p, //job arrival probability
		double C1,//queue capacity at the input of server 1
		double C2,//queue capacity at the input of server 2
		double C3,//queue capacity at the input of server 3 
		double T1,//service delay of server 1 (deterministic)
		double q2,//service probability of server 2 (geom)
		double T3,//service delay of server 3 (deterministic)
		double K1,//number of service nodes in server 1
		double K2,//number of service nodes in server 2
		double K3,//number of service nodes in server 3

		double alpha, //probability that output of s1 goes to s2.
			      //output goes to s3 with prob (1-alpha)
		
		double beta,  //probability that output of s3 goes back to s1

		double* blocking_probability,
		double* average_num_jobs_in_system,
		double* average_throughput)
{
	
	//do elaboration
	System_3_servers TOP;
	TOP.setInstanceId("TOP");
	TOP.setHierarchicalId("");

	//make a random generator and seed it
	randomGenerator = new RandomGenerator;
	randomGenerator->seedRandomEngine(rand_seed);

	//set simulation parameters
	TOP.source.p=p;
	
	TOP.s1.C=C1;
	TOP.s2.C=C2;
	TOP.s3.C=C3;
	
	TOP.s1.T=T1;
	TOP.s2.q=q2;
	TOP.s3.T=T3;
	
	TOP.s1.K=K1;
	TOP.s2.K=K2;
	TOP.s3.K=K3;

	TOP.s1.op_Q_probabilities.push_back(1.0-alpha);
	TOP.s1.op_Q_probabilities.push_back(alpha);
	
	TOP.s3.op_Q_probabilities.push_back(1.0-beta);
	TOP.s3.op_Q_probabilities.push_back(beta);

	//set h_functions for each of the embedded parameters
	TOP.s1.C_value.set_h(h_inv);
	TOP.s2.C_value.set_h(h_inv);
	TOP.s3.C_value.set_h(h_inv);

	TOP.s1.K_value.set_h(h_linear);
	TOP.s2.K_value.set_h(h_linear);
	TOP.s3.K_value.set_h(h_linear);
	
	TOP.s1.T_value.set_h(h_linear);
	TOP.s3.T_value.set_h(h_linear);

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
		current_occupancy  = TOP.s1.Q.size + TOP.s2.Q.size + TOP.s3.Q.size;
		current_occupancy += TOP.s1.ongoing_jobs + TOP.s2.ongoing_jobs + TOP.s3.ongoing_jobs;
		avg_occupancy = avg_occupancy*i/(i+1) + current_occupancy/(i+1);

		if(sitar::simulation_stopped()) break;
	};
	//compute performance metrics
	assert(i);
	assert(TOP.source.jobs_generated);
	
	*blocking_probability = ((double)TOP.source.jobs_lost)/((double)(TOP.source.jobs_generated));
	*average_num_jobs_in_system = avg_occupancy;
	*average_throughput = ((double)TOP.sink.jobs_completed)/((double)(i)) ;
	return;

}//end class definition
}//end extern C

//Just for testing:
int main()
{
	double blocking_probability=0;
	double average_num_jobs_in_system=0;
	double average_throughput=0;
	
	run_simulation(\
		42,//randomization seed
		100000,//simulation length in cycles 
		0.1, //job arrival probability
		20.0,//queue capacity at the input of server 1
		2.0,//queue capacity at the input of server 2
		2.0,//queue capacity at the input of server 3 
		5.0,//service delay of server 1 (deterministic)
		0.2,//service probability of server 2 (geom)
		2.5,//service delay of server 3 (deterministic)
		1.0,//number of service nodes in server 1
		1.0,//number of service nodes in server 2
		2.0,//number of service nodes in server 3
		0.5, //alpha, //probability that output of s1 goes to s2.
			      //output goes to s3 with prob (1-alpha)
		0.2,//beta,  //probability that output of s3 goes back to s1
		&blocking_probability,
		&average_num_jobs_in_system,
		&average_throughput);
	
	std::cout<<"\n\n Results:";
	std::cout<<"\n blocking_probability = "<<blocking_probability;
	std::cout<<"\n average_num_jobs_in_system = "<<average_num_jobs_in_system;
	std::cout<<"\n average_throughput = "<<average_throughput;
	
	return 0;
}



