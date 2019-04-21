"""
This module includes post processing functions
"""
import numpy as np
from sensitivity import test
from matplotlib import pyplot as plt
from parameters import parametrize

def plot(key):
	"""
	This function plots the sensitivity analysis results.

	Parameters
	-----
	key : str
		name of variable to be plotted

	Returns
	-----
	Saves key.png images in temp folder 
	"""
	#	Get the values of key in the var_db
	for item in var_info()[0]:
		if list(item.keys())[0] == key:
			values = item[key]

	#	Read the file corresponding to the variable
	file = np.genfromtxt('temp/'+ key + '_change_out.txt', dtype=float, delimiter=' ')

	#   Whole model runtime is summation of autoencoder and SVM runtime
	runtime = file[0,:] + file[2,:]

	#   Plot compression error (%)
	plt.subplot(1,3,1)
	plt.plot(values, file[1,:])
	plt.xlabel(key)
	plt.ylabel('Compression error (%)')

	#   Plot Classification error (%)
	plt.subplot(1,3,2)
	plt.plot(values, file[3,:])
	plt.xlabel(key)
	plt.ylabel('Classification error (%)')

	#   Plot Classification error (%)
	plt.subplot(1,3,3)
	plt.plot(values, runtime)
	plt.xlabel(key)
	plt.ylabel('Model runtime (sec)')

	#	Adjust, save and showing the plot
	plt.subplots_adjust(bottom =0.25, top=0.75, wspace=1)
	plt.savefig('temp/' + key + '.png')
	plt.show()

	return ()
