import pandas as pd
from statistics import stdev

#listcsv = ['C/C.csv', 'Java/Java.csv', 'Python/Python.csv']
listcsv = ['C/C.csv', 'Python/Python.csv']
algoritmos = ['pidigits ', 'spectral-norm ', 'fasta ', 'fannkuch-redux ', 'n-body ']

for csv in listcsv:
	print('linguagem: ', csv)
	
	arq = pd.read_csv(csv)
	
	for alg in algoritmos:
		print('algoritmo: ', alg)

		aux = arq[arq['algoritmo']==alg]
		#print(aux['energia'].mean())
		#print(aux['tempo'].mean())
		print(stdev(aux['energia']))
		print(stdev(aux['tempo']))
