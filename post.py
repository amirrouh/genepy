"""
This module includes post processing functions
"""

def test():
	"""
	This function investigates effects of different parameters on autoencoder and SVM
	runtime and accuracy.

	Parameters
	-----
	None

	Returns
	-----
	Export the results at .txt files in the temp folder
	"""
	from sensitivity import change_var
	import numpy as np

	test_samples = [{'input_dim': range(2000,22000,2000)},
		    {'epoch': range(50, 550, 10)},
		    {'batch': range(500, 5500, 500)},
		    {'latent': range(10,110,10)},
		    {'encoder_i': range(100,1050,50)},
		    {'encoder_o': range(100,1050,50)},
		    {'decoder_i': range(100,1050,50)},
		    {'decoder_o': range(100,1050,50)},
		    {'train_percent': range(50,95,5)},
		    {'lam': np.logspace(0.1, 1e-5, 10)},
		    {'c': np.logspace(1, 1e5, 10)},
		    {'norm_order': range(5, 50, 5)}]
	change_var(test_samples)
