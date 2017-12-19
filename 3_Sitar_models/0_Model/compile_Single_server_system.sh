sitar compile --no-logging  -m ./cpp/Simulate_Single_server_system.cpp  -d ./sitar_descriptions/Output/ -d ./include -o SingleServer 
mv libSingleServer.so ./lib
mv SingleServer ./exe



