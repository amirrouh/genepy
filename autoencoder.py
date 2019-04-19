def autoencoder (epoch, batch, latent, encoder_o, encoder_i, \
    decoder_i, decoder_o, train_percent, lam, norm_order, loss_plot):
    """
    This module is autoencoder neural network which gets input data and
    reduces the dimension and returns similar data to the input. Data 
    compression is useful for future data manipulation.

    Parameters
    ----------
    epoch  : int
        Epoch gets the epoch number of the neural network passed through
        the neural network in each iteration
    batch  : int
        Batch number of the neural network determines how many times all 
        the data will be passed through the neural network
    latent : int
        Latent vector dimension shows the size of buttleneck (compressed data)
    encoder_o : int
        Size of outer encoder hidden layer of the neural network close to the 
        input
    encoder_i : int
        size of inner encoder hidden layer of the neural network close to the 
        buttleneck
    decore_i : int
        size of inner decoder hidden layer of the neural network close to the 
        buttleneck
    decore_o : int
        size of outer decoder hidden layer of the neural network close to the 
        output
    train_percent : float
        (The value will be between 0 and 100) shows what fraction of the dataset
        will be used for training and the rest for testing
    lam : float
        The coefficient of regularization for the autoencoder model
    norm_order: int 
        keras data normalization parameter
    loss_plot : Boolean
        If True plots the loss function and if False, does not plot that

    Returns
    -------
    input : list
        gives all the inputs used for training
    latent vector : list
        Latent vector, the compressed representation of the input
    reconstructed: list
        Gives the reconstructed data from the input  
    cell_types: list
        Gives a list of integers represent cell types for the given input data
    runtime : float
        Training runtime in seconds
    error: float
        The autoencoder average error (%)
    """
    #   Import required libraries
    from keras import callbacks
    from keras.layers import Input, Dense
    from keras.models import Model
    from keras.utils import normalize
    from keras import regularizers
    import tensorflow as tf
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.pyplot import draw, show
    import pickle
    import time

    #   starting time is measured to compare performance"""
    time_start = time.time()

    #   Importing the database parsed from the input file
    dataset = np.load('temp/dataset_binary.npy')

    #   PErforme log transform and normalization before analysis
    input_data =np.log(dataset[:,:-1]) / np.log(2)
    input_data = normalize(input_data, axis=0, order=norm_order)
    input_size = len(input_data[0, :])

    #   Split cell types list from the raw data and keep it
    labels = dataset[:,-1]

    #   Split training and testing data from the input dataset
    percent_training = int(len(input_data[:, 0]) * (train_percent/100))
    X_train = input_data[:percent_training,:input_size]
    L_train = dataset[:percent_training, -1]
    X_test = input_data [percent_training:,:input_size]
    L_test = dataset[percent_training:, -1]

    #   Define network parameters
    epoch_size = epoch
    batch_size = batch
    latent_dim = latent

    #   Lambda coefficnet of l2 regulizor of the keras
    lam = lam

    ### Building the neural network layers
    encoder_o = encoder_o
    encoder_i = encoder_i
    decoder_i = decoder_i
    decoder_o = decoder_o

    #   building the input layer
    input_gene_expression = Input(shape=(input_size,))

    """#### Encoder layer
    The encoder layer will connet input layer to the latent vector.
    In order to avoid ovefitting, l2 regularization methos is used which 
    changes loss function for larger weights.
    """
    encoded = Dense(encoder_o, kernel_regularizer=regularizers.l2(lam), \
        activation=tf.nn.relu)(input_gene_expression)
    encoded = Dense(encoder_i, kernel_regularizer=regularizers.l2(lam), \
        activation=tf.nn.relu)(encoded)
    encoded = Dense(latent_dim, kernel_regularizer=regularizers.l2(lam), \
        activation=tf.nn.relu)(encoded)

    """#### Decoder layer
    Decoder layer is defined same as encoder layer but, it connects latent space
     to the output layer.
    """
    decoded = Dense(decoder_i, kernel_regularizer=regularizers.l2(lam), \
        activation =tf.nn.relu)(encoded)
    decoded = Dense(decoder_o, kernel_regularizer=regularizers.l2(lam), \
        activation =tf.nn.relu)(decoded)
    decoded = Dense(input_size, kernel_regularizer=regularizers.l2(lam), \
        activation =tf.nn.sigmoid)(decoded)

    """
    The autoencoder model is created mapping input data to reconstructed data 
    similar to the input.
    """
    autoencoder = Model(input_gene_expression, decoded)

    """
    Encoder model is created to show the latent vectors
    """
    encoder = Model(input_gene_expression, encoded)
    
    """
    Loss function of variational autoencoder is defined as the distance between
    input and output using mean squared error (MSE). The optimizer "adam" is 
    then used to minimize the MSE function
    """
    autoencoder.compile(optimizer='adam', loss='mean_squared_error',metrics=\
        ['accuracy'])
    

    """
    Training the autoencoder model: Network dimensions, batch and epoch sizes 
    and training and testing datasets are used to train the model
    """

    #   This section defins the plot and callback functions to track training
    class PlotLosses(callbacks.Callback):
        def on_train_begin(self, logs={}):
            self.i = 0
            self.x = []
            self.losses = []
            self.val_losses = []
            
            self.fig = plt.figure()
            
            self.logs = []

        def on_epoch_end(self, epoch, logs={}):
            self.logs.append(logs)
            self.x.append(self.i)
            self.losses.append(logs.get('loss'))
            self.val_losses.append(logs.get('val_loss'))
            self.i += 1

            if loss_plot:
                plt.plot(self.x, self.losses, label="Training loss", c = 'b', \
                    linestyle = '-')
                plt.plot(self.x, self.val_losses, label="Validation loss",\
                     c = 'b', linestyle = '-.')
                plt.pause(0.01)
                plt.title('Training loss: ---, Validation loss: -.-.')
                plt.xlabel('Epoch number')
                plt.ylabel('MSE value')
        
            else:
                pass


    time_start = time.time()
    autoencoder.fit(X_train, X_train, epochs=epoch_size, batch_size=batch_size,\
                    shuffle=True, callbacks=[PlotLosses()], validation_data=\
                        (X_test, X_test), verbose=1)


    #   Build reconstructed testing layer to measure the autoencoder's error
    reconstructed_test = autoencoder.predict(X_test)
 
    #   Autoencoder training runtime is calculated
    time_end = time.time()
    auto_runtime = time_end - time_start


    #   Autoencoder error is defined
    diff = abs(X_test - reconstructed_test)
    diff_mean = np.mean(diff)
    mean = np.mean(abs(X_test))
    auto_err = diff_mean / mean

    #   show() function, keeps the plot open until the computation is finished
    if loss_plot:
        show()
    else:
        pass

    #   Build latent and reconstruction tensors
    latent = encoder.predict(input_data)
    reconstructed = autoencoder.predict(input_data)

    #   exporting latent file and labels for classifier
    pickle.dump(latent, open('temp/latent', 'wb'))
    pickle.dump(labels, open('temp/labels', 'wb'))
    
    return input_data, latent, reconstructed, labels, auto_runtime, auto_err
