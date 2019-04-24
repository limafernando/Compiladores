compile:
	cp fasta.python3-3.python3 fasta.python3-3.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/local/bin/python3.6 -OO fasta.python3-3.py 2500000" Python fasta

run:
	/usr/local/bin/python3.6 -OO fasta.python3-3.py 2500000

mem:
	/usr/local/bin/python3.6 -OO fasta.python3-3.py 2500000
