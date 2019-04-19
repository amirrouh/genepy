def classify (gamma, c, train_percent):
    """
    This module uses support vector machine (SVM) to classify the cell types 
    based on their compressed gene expression profile (latent vectors)

    Parameters
    ----------
    gamma  : float
        C-support nonlinear SVM Parameter (Gamma)
    c : float
        C-support nonlinear SVM Parameter (C)
    percent : float
        show what percentage is used for training (between 0 and 100)

    Returns
    -------
    label_predicted: list
        List of label predictions
    svm_runtime : loat
        SVM runtime in seconds
    svm_err : float
        SVM average error (%)
    """
    #   Import required libraries
    from sklearn import svm
    import numpy as np
    import pickle
    import time


    #   Start time to measure SVM runtime
    time_start = time.time()

    #   Import latent data and labels (created by the autoencoder)
    latent = pickle.load(open('temp/latent', 'rb'))
    labels = pickle.load(open('temp/labels', 'rb'))

    #   Prepare testing and training datasets
    input_size = len(latent[0, :])
    percent_training = int(len(latent[:, 0]) * (train_percent/100))
    latent_train = latent[:percent_training,:input_size]
    label_train = labels[:percent_training]
    latent_test = latent[percent_training:,:input_size]
    label_test = labels[percent_training:]

    #   SVM training function
    def cell_classifier(input):
        model = svm.SVC(gamma=gamma, C=c)
        model.fit(latent_train, label_train)
        output = model.predict(input)
        return output

    #   Make predictions based on the testing latent vectors
    label_predicted = cell_classifier(latent_test)

    #   Classification error calculation
    missclassified = np.count_nonzero(label_test - label_predicted)
    svm_err = missclassified / len(label_test)


    #   SVM Runtime is measured
    time_end = time.time()
    svm_runtime = time_end - time_start

    return label_predicted, svm_runtime, svm_err
