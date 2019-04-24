compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/lua5.3  nbody.lua-2.lua 50000000" Lua n-body

run:
	/usr/bin/lua5.3  nbody.lua-2.lua 50000000

mem:
	/usr/bin/time -v  /usr/bin/lua5.3  nbody.lua-2.lua 50000000

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/lua5.3  nbody.lua-2.lua 50000000
