cd ./sitar_descriptions
./translate_all.sh
cd -
sitar compile --no-logging  -m ./cpp/Simulate_Single_server_system.cpp  -d ./sitar_descriptions/Output/ -d ./include --cflags '-fPIC -DGENERATE_SHARED_LIBRARY_ONLY -std=c++0x' -o SingleServer 
mv libSingleServer.so ./lib
mv SingleServer ./exe



