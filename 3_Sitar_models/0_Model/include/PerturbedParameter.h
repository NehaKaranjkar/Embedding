#ifndef PERTURBED_PARAMETER_H
#define PERTURBED_PARAMETER_H


#include<cmath>
#include<cassert>
#include"RandomGenerator.h"




// Class PerturbedParameter is used to model 
// a discrete random variable 



class PerturbedParameter
{
	public:
		double y;  //the assigned continuous value
		int instantaneous_value; //instantaneous value of the rand variable
		bool y_is_int; //true when y is an integer

		//randomization parameters:
		double r;
		double s;
		std::vector<int> stencil;
		std::vector<double> alphas;
		std::discrete_distribution<int>* distribution;

	public:
		
		//constructor
		PerturbedParameter()
		{
			y=0.0;
			instantaneous_value=0;
			y_is_int=true;

			r=1.0;
			s=1.0;
			distribution = NULL;
			
		};
		
		double L_floor(double value)
		{
			double a = value - floor(value)+1.0;
			double b = 2.0;
			double l_f = pow( (fabs(pow(a,s) - pow(b,s))), r);
			return l_f;
		}
		
		double L_ceil(double value)
		{
			double a = value - floor(value)+1.0;
			double b = 1.0;
			double l_c = pow( (fabs(pow(a,s) - pow(b,s))), r);
			return l_c;
		}
			
		double get_alpha(double value)
		{
			//calculate probability alpha
			double alpha = L_floor(value)/(L_floor(value)+ L_ceil(value));
			assert(alpha>=0 and alpha<1);
			return alpha;
		};

		void initialize(int stencil_size, double r_val, double s_val, double y_val)
		{
			r = r_val;
			s = s_val;
			y = y_val;

			//get stencil:
			//	currently we're
			//	hardwired at stencil_size=2.
			//	The stencil-size argument is ignored.
			if(floor(y)==ceil(y))
			{
				stencil.push_back(int(y));
				alphas.push_back(1.0);
				instantaneous_value=int(y);
				y_is_int=true;
			}
			else
			{
				double alpha = get_alpha(y);
				stencil.push_back(floor(y));
				alphas.push_back(alpha);
				
				stencil.push_back(ceil(y));
				alphas.push_back(1.0-alpha);

				distribution = new std::discrete_distribution<int> (alphas.begin(),alphas.end());
				instantaneous_value = stencil[(*distribution)(randomGenerator->randomEngine)];
				y_is_int = false;
			}
		}
	
	
		//set instantaneous value : 
		//called once every cycle to set instantaneous value 
		//of the parameter for this cycle
		long int setInstantaneousValue()
		{
			if (y_is_int==true)
				return instantaneous_value;
			else
			{
				instantaneous_value = stencil[(*distribution)(randomGenerator->randomEngine)];
				return instantaneous_value;
			}
		}
			
		inline long int getInstantaneousValue(){return instantaneous_value;};

};

#endif

