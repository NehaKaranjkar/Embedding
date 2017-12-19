//Occupancy.h
//
//A data-structure to record the occupancy of a server
//for T cycles.
//
//Author: Neha Karanjkar
//Date  : March 2016

#ifndef OCCUPANCY_H
#define OCCUPANCY_H
#include<cassert>
#include<cstddef>

class Occupancy
{
	public:
		int* buffer; 	//buffer for storing occupancy
		int size;	//size of the buffer
		
		//index of the current head of the buffer
		int head;
			
		//Constructor
		Occupancy()
		{
			buffer=NULL;
			size=0;
			head=0;
		}
		
		//destructor
		~Occupancy()
		{
			delete[] buffer;
		}
		
		//Initilization/reset function
		void initialize(int _size)
		{
			assert(_size);
			size=_size;

			delete[] buffer;
			buffer=new int[size];
			assert(buffer);
			//Initialize all elements to 0		
			for(int i=0;i<size;i++)
				buffer[i]=0;
			head=0;
		}
		
		//Constructor with a size parameter
		Occupancy(int _size)
		{
			buffer=NULL;
			size=0;
			head=0;
			initialize(_size);

		}

		
		//get occupancy for the current cycle
		int get()
		{
			assert(buffer);
			return buffer[head];
		}


		//increment occupancy for 
		//the current cycle and T-1 cycles in future
		void increment(int T)
		{
			assert(T>=1 && T<=size);
			assert(buffer);
			//increment the values in the buffer
			//for T elements, starting from head
			for(int i=0;i<T;i++)
			{
				buffer[((head+i)%size)]++;
			}
		}

		void shiftLeft()
		{
			assert(buffer);
			

			////print out the occupancy list for debugging
			//	std::cout<<"\n Occupancy :";
			//	for(int i=0;i<size;i++)
			//	{
			//		std::cout<<" "<<buffer[((head+i)%size)];
			//	}

			//shift the buffer left
			//reset the element at the head
			buffer[head]=0;
			//move the head right
			head=(head+1)%size;
		
		}


};


class EndTime : public Occupancy
{
	//Identical to the Occupancy class, 
	//except that the increment function
	//increments only one element at T,
	//not all elements from head to T
	public:
		void increment(int T)
		{
			assert(T>=1 && T<=size);
			assert(buffer);
			//increment the values in the buffer
			//for exactly one element at T-1
			int i=T-1;
			buffer[((head+i)%size)]++;
		}	
		
		//Constructor with a size parameter
		EndTime(int _size)
		{
			buffer=NULL;
			size=0;
			head=0;
			initialize(_size);
		}
};

#endif
