# Embedding
Embedding discrete parameters in discrete-time queues.


There are two versions of the discrete-time queueing models:

1. Models written using SimPY. 
	
	Folder: ./2_SimPy_models
	
	Requirements:
		Python3
		SimPY v3.0 (https://simpy.readthedocs.io/en/latest/)

2. Models written using Sitar, which is a cycle-based modeling framework.
The models written in Sitar seem to run about 200X faster than their SimPy versions.
	
	Folder: ./3_Sitar_models

	Requirements:
		C++11
		Sitar (https://nehakaranjkar.github.io/sitar/)

