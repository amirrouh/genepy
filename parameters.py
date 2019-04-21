def parametrize(parameter, value):
    """
    This module has all the parameter needed to run the model

    Parameters
    ----------
    parameter: str
        Parameters name which is to be changed
    value: NA
        Value of the parameter which is changing

    Returns
    -------
    parameters : dict
        Return a dictionary of all the parameters and the values
    """

    #   Server parameters
    parameters = {'directory_1':'local_directory',
        'directory_2': 'directory_on_server',
        'key_address': 'full_address_to_the_ssh_key_file',
        'user': 'username', 'server': 'server address',\

    #   Parsing parameters
        'link': 'ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/GDS1nnn/GDS1615/soft/GDS1615_full.soft.gz',
        'input_dim': 2000,\

    #   Autoencoder parameters
        'epoch': 200, 'batch': 200, 'latent': 30, 'encoder_o': 300,
        'encoder_i': 100, 'decoder_i': 100, 'decoder_o': 300, 'train_percent': 75,
        'lam': 0.0001, 'loss_plot': False, 'norm_order': 10,\

    #   SVM parameters
        'train_percent' : 75, 'gamma': 0.0001, 'c' : 1000000}

    parameters[parameter] = value


    keys = list(parameters.keys())
    values = list(parameters.values())




    #   Returns the list of lictionaries for post module
    packed = []
    for i in range(len(keys)):
        key = [keys[i]]
        value = [values[i]]
        packed.append(dict(zip(key, value)))
    
    return parameters, packed
