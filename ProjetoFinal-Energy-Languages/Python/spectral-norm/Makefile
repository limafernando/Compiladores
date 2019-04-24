compile:
	cp spectralnorm.python3-5.python3 spectralnorm.python3-5.py
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/local/bin/python3.6 -OO spectralnorm.python3-5.py 5500" Python spectral-norm

run:
	/usr/local/bin/python3.6 -OO spectralnorm.python3-5.py 5500

mem:
	/usr/local/bin/python3.6 -OO spectralnorm.python3-5.py 5500
