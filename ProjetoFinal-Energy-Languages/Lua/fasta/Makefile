compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/lua5.3  fasta.lua-3.lua 2500000" Lua fasta

run:
	/usr/bin/lua5.3  fasta.lua-3.lua 2500000

mem:
	/usr/bin/time -v  /usr/bin/lua5.3  fasta.lua-3.lua 2500000

valgrind:
	valgrind --tool=massif --stacks=yes  /usr/bin/lua5.3  fasta.lua-3.lua 2500000
