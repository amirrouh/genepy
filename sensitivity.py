"""
This module includes sensitivity analyis function to measure autoencoder and SVM
accuracy and performance
"""


def change_var(parameter, values)
    """
    This module changes a parameters by the values provided and returns 
    autoencoder and SVM runtime and errors.

    parameter: str
    ----------
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

    from parse import read
    from autoencoder import autoencoder
    from svm import classify
    from bash import connect
    from parameters import parametrize


    def whole_model(parameters):
        read(link, input_dim)
        _, _, _, _, auto_runtime, auto_err = \
            autoencoder(epoch, batch, latent,
                        encoder_o, encoder_i, decoder_i, decoder_o, train_percent, lam,
                        norm_order, loss_plot)

        _, svm_runtime, svm_err = classify(gamma, c, train_percent)
        return auto_runtime, auto_err, svm_runtime, svm_err


    parameter = 'latent'
    values = range(10, 30, 10)


    auto_runtime, auto_err, svm_runtime, svm_err = [], [], [], []

    for v in values:
        parameters = parametrize(parameter, v)
        locals().update(parameters)
        a_runtime, a_err, s_runtime, s_err = whole_model(parameters)
        auto_runtime.append(a_runtime)
        auto_err.append(a_err)
        svm_runtime.append(s_runtime)
        svm_err.append(a_err)
    
    return auto_runtime, auto_err, svm_runtime, svm_err
