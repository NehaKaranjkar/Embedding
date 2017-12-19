#ifndef QUEUE_H
#define QUEUE_H
#include<cassert>
#include"PerturbedParameter.h"


//Queue
//If the function setCapacity is called,
//then the queue behaves as a finite capacity queue.
//else it behaves as an infinite capacity queue
//
//
//The parameter queue capacity has been embedded
//into continuous space.


class Queue
{
	public:
		long unsigned int size;  //current size of queue
		bool finite_capacity;	//if true, the capacity parameter is used, else queue
					//is assumed to be of infinite capacity
		long unsigned int capacity; 	
				
		//constructor
		Queue() 
		{ 
			size=0;
			finite_capacity=false;
			capacity=1; 
			total_utilization=0; 
			samples_taken=0;
		};
		
		inline void setCapacity(long unsigned int cap) 
		{ 
			finite_capacity=true;
			capacity=cap; 
		};
		
		inline int getRemainingCapacity() 
		{
			if(finite_capacity)
			{
				long int remaining_cap = capacity-size; 
				if(remaining_cap < 0) return 0;
				else return remaining_cap;
			}
			else
			{
				return 1;
			}
		};


		inline bool push()
		{
			if(finite_capacity and getRemainingCapacity()<=0)
				return false;
			else
			{
				size++;
				return true;
			}
		};
		
		inline bool pull()
		{
			
			if(size==0)
				return false;
			else
			{
				size--;
				return true;
			}
		};

		inline bool empty()
		{
			if( size==0) return true;
			else return false;
		};
		
		inline bool full()
		{
			if( finite_capacity and size>=capacity) return true;
			else return false;
		};

		
		//variables for measuring utilization of the queue
		double total_utilization;
		double samples_taken;    
		inline void updateUtilizationCount()
		{
			total_utilization += size;
			samples_taken +=1;
		}
		inline double getAverageSize()
		{
			if(samples_taken ==0) return size;
			else return (total_utilization/samples_taken);
		}
};
#endif

