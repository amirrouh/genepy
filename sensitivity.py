"""
This module includes sensitivity analyis function to measure autoencoder and SVM
accuracy and performance
"""


def change_var(parameter, values):
    """
    This module changes a parameters by the values provided and returns 
    autoencoder and SVM runtime and errors.

    parameters
    ----------
    parameter: str
        Parameters name which is to be changed
    value: NA
        Value of the parameter which is changing

    Returns
    -------
    [auto_runtime, auto_err, svm_runtime, svm_err]
    
    where:

    auto_runtime : float
        Autoencoder runtime in seconds
    auto_err : float
        Autoencoder average error in percentage
    svm_runtime : float
        SVM runtime in second
    svm_err : float
        SVM average error in percentage
    """
    #   Import required libraries
    from parse import read
    from autoencoder import autoencoder
    from svm import classify
    from bash import connect
    from parameters import parametrize


    #   Run the functions to assess performance, the inputs are passed in shape of dictionary
    def whole_model(**kwargs):
        read(kwargs['link'], kwargs['input_dim'])
        _, _, _, _, auto_runtime, auto_err = \
            autoencoder(kwargs['epoch'], kwargs['batch'], kwargs['latent'],
                        kwargs['encoder_o'], kwargs['encoder_i'], kwargs['decoder_i'], 
                        kwargs['decoder_o'], kwargs['train_percent'], kwargs['lam'], 
                        kwargs['norm_order'], kwargs['loss_plot'])
        _, svm_runtime, svm_err = classify(kwargs['gamma'], kwargs['c'], kwargs['train_percent'])
        return auto_runtime, auto_err, svm_runtime, svm_err


    auto_runtime, auto_err, svm_runtime, svm_err = [], [], [], []

    for v in values:
        parameters = parametrize(parameter, v)
        #   Here **, unzips parameters dictionary to argument before passing to the function
        a_runtime, a_err, s_runtime, s_err = whole_model(**parameters)
        auto_runtime.append(a_runtime)
        auto_err.append(a_err)
        svm_runtime.append(s_runtime)
        svm_err.append(a_err)
    
    return auto_runtime, auto_err, svm_runtime, svm_err
