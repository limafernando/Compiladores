compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/lua5.3  fannkuchredux.lua 12" Lua fannkuch-redux

run:
	/usr/bin/lua5.3  fannkuchredux.lua 12

mem:
	/usr/bin/time -v /usr/bin/lua5.3  fannkuchredux.lua 12

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/lua5.3  fannkuchredux.lua 12
