"""
This module includes post processing functions
"""
import numpy as np
from sensitivity import change_var
from matplotlib import pyplot as plt

#	Tesing variables are defined here 
def var_info():
	"""
	This function stores variable and their ranges

	Parameters
	-----
	None

	Returns
	-----
	var_db : dic
		Gives variables and values used for testing
	var_names: list
		Gives variable names as a list
	var_values: list
		Gives variable values as a list
	"""
	var_db = [{'input_dim': range(2000,22000,2000)},
			{'epoch': range(50, 550, 10)},
			{'batch': range(500, 5500, 500)},
			{'latent': range(10,110,10)},
			{'encoder_i': range(100,1050,50)},
			{'encoder_o': range(100,1050,50)},
			{'decoder_i': range(100,1050,50)},
			{'decoder_o': range(100,1050,50)},
			{'train_percent': range(50,95,5)},
			{'lam': np.logspace(0.1, 1e-5, 10, endpoint=True)},
			{'c': np.logspace(1, 1e5, 10, endpoint=True)},
			{'norm_order': range(5, 50, 5)}]

	var_names, var_values = [], []
	for item in var_db:
		var_names.append(list(item.keys())[0])
		var_values.append(list(item.values())[0])

	return var_db, var_names, var_values


def test():
	"""
	This function investigates effects of different parameters on autoencoder and SVM
	runtime and accuracy.

	Parameters
	-----
	None

	Returns
	-----
	Saves *.txt files in temp folder including the sensitivity analyisis results
	"""
	test_samples, _, _ = var_info()
	change_var(test_samples)

	return test_samples


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
