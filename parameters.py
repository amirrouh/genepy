def database():
    """
    This module has all the parameters and values

    Parameters
    ------

    Returns
    -------
    parameters : dict
        Return a dictionary of all the parameters and the values
    """
    #   Server parameters
    parameters = {'directory_1': 'local_directory',
                  'directory_2': 'directory_on_server',
                  'key_address': 'full_address_to_the_ssh_key_file',
                  'user': 'username', 'server': 'server address',

                  #   Parsing parameters
                  'link': 'ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/GDS1nnn/GDS1615/soft/GDS1615_full.soft.gz',
                  'input_dim': 500,\

                  #   Autoencoder parameters
                  'epoch': 50, 'batch': 200, 'latent': 30, 'encoder_o': 100,
                  'encoder_i': 50, 'decoder_i': 50, 'decoder_o': 100, 'train_percent': 75,
                  'lam': 0.0001, 'loss_plot': False, 'norm_order': 10,\

                  #   SVM parameters
                  'train_percent': 75, 'gamma': 0.0001, 'c': 1000000}

    keys = list(parameters.keys())
    values = list(parameters.values())

    #   converts the long dictionary to list of small dictionaries consist of a variable and values
    packed = []
    for i in range(len(keys)):
        key = [keys[i]]
        value = [values[i]]
        packed.append(dict(zip(key, value)))

    return parameters, packed


def parametrize(parameter, value):
    """
    This module changes the parameter needed to run the model

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

    #   Read the database as a big dictionary and change the values and retuns big
    #   dictionary and list of small dictionatries
    parameters, _ = database()

    parameters[parameter] = value

    keys = list(parameters.keys())
    values = list(parameters.values())

    #   converts the long dictionary to list of small dictionaries consist of a variable and values
    packed = []
    for i in range(len(keys)):
        key = [keys[i]]
        value = [values[i]]
        packed.append(dict(zip(key, value)))

    return parameters, packed
