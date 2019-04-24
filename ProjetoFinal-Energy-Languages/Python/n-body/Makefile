compile:
	cp nbody.python3 nbody.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/local/bin/python3.6 -OO nbody.py 50000000" Python n-body

run:
	/usr/local/bin/python3.6 -OO nbody.py 50000000

mem:
	/usr/local/bin/python3.6 -OO nbody.py 50000000
