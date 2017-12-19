#ifndef RANDOM_GENERATOR_H
#define RANDOM_GENERATOR_H

//RandomGenerator.h

#include<random>

class RandomGenerator
{
	public:
		std::default_random_engine  randomEngine;
		std::uniform_real_distribution<double> d;

		//constructor
		RandomGenerator(): d(0,1.0){};

		inline void seedRandomEngine(double my_seed )
		{
			randomEngine.seed(my_seed);

		};

		inline double randNumBetween0and1()
		{
			// returns a random num between 0 and 1
			// with uniform distribution, using a global engine
			return d(randomEngine);
		};
		
		inline double get()
		{
			// returns a random num between 0 and 1
			// with uniform distribution, using a global engine
			return d(randomEngine);
		};

};


//somebody (mostly main.cpp) will create an object 
//and set pointer randomGenerator to point to it.
extern RandomGenerator* randomGenerator;

#endif

