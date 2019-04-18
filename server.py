def sync(directory_1, directory_2, key_address, user, server):
    """
    This module creates a bash script to compressed desired files and folders and copies 
    them to the UCF Clusters. For security purposes, this module does not save passwords 
    or passphrases

    Parameters
    ----------
    directory_1 : str
        This arg gives the folder we want to sync on local machine
        (1.e. '~/Dropbox/python/')
    directory_2 : str
        destination address on the server 
        (i.e. '~/Dropbox/')
    key_address : str
        This are gets full address of the secure key file 
        (i. e. '~/Dropbox/stokes/arouhollahi-keys/arouhollahi_id_rsa_1')
    user : str
        Username
        
    server: str
        Server address
        (i.e. )

    returns:
        sync.sh bash file to run using sh sync.sh in the terminal
    """

    import os
    #   Creates a list of files in the working directory
    files = os.listdir()


    # If the bash file already exists, it deletes the bash file before making progress
    if 'sync.sh' in files: 
        os.remove('sync.sh')
    else:
        pass


    with open('sync.sh', 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('zip -r my_files.zip ' + str(directory_1) + '\n')
        f.write('scp -i ' + str(key_address) + ' my_files.zip ' + str(user) + \
            '@' + str(server) + ':' + str(directory_2))
