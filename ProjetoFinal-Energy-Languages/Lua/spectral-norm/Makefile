compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/lua5.3  spectralnorm.lua 5500" Lua spectral-norm

run:
	/usr/bin/lua5.3  spectralnorm.lua 5500

mem:
	/usr/bin/time -v /usr/bin/lua5.3  spectralnorm.lua 5500

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/lua5.3  spectralnorm.lua 5500
