#ifndef PERTURBED_PARAMETER_H
#define PERTURBED_PARAMETER_H


#include<cmath>
#include<cassert>
#include"RandomGenerator.h"
#include<stdio.h>



// Class PerturbedParameter is used to model 
// a discrete random variable 

#define ZERO (double(0.0))
#define ONE (double(1.0))
#define TWO (double(2.0))
#define EPS (std::numeric_limits<double>::epsilon())
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
			double a = value - floor(value)+ ONE;
			double b = TWO;
			double l_f = pow( (fabs(pow(a,s) - pow(b,s))), r);
			return l_f;
		}
		
		double L_ceil(double value)
		{
			double a = value - floor(value) + ONE;
			double b = ONE;
			double l_c = pow( (fabs(pow(a,s) - pow(b,s))), r);
			return l_c;
		}
				

		double get_alpha(double value)
		{
			//calculate probability alpha
			double alpha = L_floor(value)/(L_floor(value)+ L_ceil(value));
			assert(alpha > ZERO and alpha <= ONE);
			return alpha;
		};

		void initialize(int stencil_size, double r_val, double s_val, double y_val)
		{
			r = r_val;
			s = s_val;
			y = y_val;

			(void)stencil_size; //mark unused
			//	currently we're
			//	hardwired at stencil_size=2.
			//	The stencil-size argument is ignored.
			
			
			//split y into an int and fractional part
			double y_fract, y_int;
			y_fract = modf (y, &y_int);

			if(y_fract < EPS)
			{	
				//y is very very close to floor(y)
				stencil.push_back(int(y_int));
				alphas.push_back(ONE);
				instantaneous_value=int(y_int);
				y_is_int=true;
			}
			else if((ONE-y_fract) < EPS)
			{	
				//y is very very close to ceil(y)
				stencil.push_back(int(y_int)+1);
				alphas.push_back(1.0);
				instantaneous_value=int(y_int)+1;
				y_is_int=true;
			}
			else
			{
				double alpha = get_alpha(y);
				stencil.push_back(floor(y));
				alphas.push_back(alpha);
				
				stencil.push_back(ceil(y));
				alphas.push_back(ONE-alpha);

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

