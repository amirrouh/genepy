def param():
    """
    This module has all the parameter needed to run the model

    Parameters
    ----------

    Returns
    -------

    """

    #   Server parameters
    param = {'directory_1':'folder_address_you_want_to_sync_on_your_machine',
        'directory_2': 'folder_address_you_want_to_sync_on_the server',
        'key_address': 'full_address_to_your_key_file',
        'user': 'your_username', 'server': 'newton.ist.ucf.edu',\

    #   Parsing parameters
        'link': 'ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/GDS1nnn/GDS1615/soft/GDS1615_full.soft.gz',
        'input_dim': 2000,\

    #   Autoencoder parameters
        'epoch': 200, 'batch': 200, 'latent': 30, 'encoder_o': 300,
        'encoder_i': 100, 'decoder_i': 100, 'decoder_o': 300, 'train_percent': 75,
        'lam': 0.0001, 'loss_plot': False, 'norm_order': 10,\

    #   SVM parameters
        'train_percent' : 75, 'gamma': 0.0001, 'c' : 1000000}
