"""
This module downloads gene expression profile from NCBI GEO FTP website and parses it
Parameters
----------
link  : str
  This is the link to GEO soft_full.gz file on NCBI website
file  : str
  File name checks whether the file is downloaded before, in that case it will does not download the file again
  
Returns
-------
This modules save three foloowing pickle files into temp folder in the working directory 
sd  : list
  Subset descriptions
si  : list
  Subset Indices for subset discriptions, to load one discription indices, (i.e. to load a list of 
  subset indices for the n_th subset description, use: si[n])
ge  : pandas dataframe
  Gene expression values and a numpy array
"""


def read_geo(link):
    import gzip
    import numpy as np
    import pandas as pd
    import pickle
    from matplotlib.pyplot import plot as plt
    import os
    
    file_name = link.split('/')[-1]
    dir_root = os.listdir()

    if 'temp' not in dir_root: 
        os.mkdir('temp')
    else:
        pass 

    dir_temp = os.listdir('temp/')

    # If the input file does not exist then it will download the file, otherfiles, 
    # the code will use the existing file
    if file_name not in dir_temp: 
        import urllib.request
        urllib.request.urlretrieve(link, 'temp/' + file_name)[0]

    else:
        pass

    # Data input dimension to simplify is defined (None => imports all the genes unless number of genes are declared)
    data_dim = None

    with gzip.open('temp/' + file_name, 'rt') as f:
        #    sd: subset description
        #    si: subset id
        #    ge: gene expression
        sd, si, ge = [], [], []
        
        #    Obtain subset description
        for line in f:
            if "!subset_description" in line:
                sd.append(line.split('=')[1].strip())
                
            elif "!subset_sample_id" in line:
                si.append(line.split('=')[1].strip().split(','))
                
            elif "!dataset_table_begin" in line:
                break
            
        subset_number = sum(len(sd) for sd in si)
        #  Read the gene info table

        for line in f:
            if "!dataset_table_begin" in line:
                break            
    
            elif "!dataset_table_end" in line:
                break
    
            ge.append(line.split()[:2 + subset_number])
    
    ge = pd.DataFrame(ge)
    new_header = ge.iloc[0]
    ge.columns = new_header
    ge = ge[1:]


    #   Here, we create a temporary directory to store needed files
    ge.to_pickle('temp/ge')
    pickle.dump(sd , open( 'temp/sd', 'wb' ))
    pickle.dump(si , open( 'temp/si', 'wb' ))

    return
