compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/lua5.3  pidigits.lua-5.lua 10000" Lua pidigits

run:
	/usr/bin/lua5.3  pidigits.lua-5.lua 10000

mem:
	/usr/bin/time -v /usr/bin/lua5.3  pidigits.lua-5.lua 10000


valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/lua5.3  pidigits.lua-5.lua 10000

