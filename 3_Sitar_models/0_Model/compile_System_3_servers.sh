#for f in *.sitar; do sitar translate "$f"; done

sitar compile --no-logging  -m ./cpp/Simulate_System_3_servers.cpp  -d ./sitar_descriptions/Output/ -d ./include --cflags '-fPIC -DGENERATE_SHARED_LIBRARY_ONLY -std=c++0x'  -o System_3_servers

mv libSystem_3_servers.so ./lib
mv System_3_servers ./exe

