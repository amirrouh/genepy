"""
This module includes post processing functions
"""
import numpy as np
from sensitivity import test
from matplotlib import pyplot as plt
from parameters import database

def plot_run(parameter, values):
	"""
	This function plots the sensitivity analysis results.

	Parameters
	-----
	parameter : str
		name of variable to be plotted
	values: list
		list of values for the above variable

	Returns
	-----
	Saves key.png images in temp folder 
	"""
	#	Read the file corresponding to the variable
	file = np.genfromtxt('temp/'+ parameter + '_change_out.txt', dtype=float, delimiter=' ')

	#   Whole model runtime is summation of autoencoder and SVM runtime
	runtime = file[0,:] + file[2,:]

	#   Plot compression error (%)
	plt.subplot(1,3,1)
	plt.plot(values, file[1,:])
	plt.xlabel(parameter)
	plt.ylabel('Compression error (%)')

	#   Plot Classification error (%)
	plt.subplot(1,3,2)
	plt.plot(values, file[3,:])
	plt.xlabel(parameter)
	plt.ylabel('Classification error (%)')

	#   Plot Classification error (%)
	plt.subplot(1,3,3)
	plt.plot(values, runtime)
	plt.xlabel(parameter)
	plt.ylabel('Model runtime (sec)')

	#	Adjust, save and showing the plot
	plt.subplots_adjust(bottom =0.25, top=0.75, wspace=1)
	plt.savefig('temp/' + parameter + '.png')
	plt.show()

	return ()


def plot(test_params):
	for item in test_params:
		key = list(item.keys())[0]
		values = list(item.values())[0]
		plot_run(key, values)