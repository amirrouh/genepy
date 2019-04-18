"""
This module Downloading gene expression profile from NCBI GEO FTP website

Parameters
----------
link  : str
  This is the link to GEO soft_full.gz file on NCBI website

file  : str
  File name checks whether the file is downloaded before, in that case it will does not download the file again
  
Returns
-------
sd  : str
  Subset description
si  : list
  Subset Index
ge  : numpy array
  Gene expression values and a numpy array

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""


def model(link):
    import gzip
    import numpy as np
    import pandas as pd
    from matplotlib.pyplot import plot as plt
    import os
    
    files = os.listdir()

    # If the files does not exist then it will download the file, otherfiles, the code will use the existing file
    if 'GDS1615_full.soft.gz' not in files: 
        import urllib.request
        file_name = urllib.request.urlretrieve(link, link.split('/')[-1])[0]

    else:
        file_name ='GDS1615_full.soft.gz' 


    def read_geo(file_name, subset_description):
        # Data input dimension to simplify is defined (None => imports all the genes unless number of genes are declared)
        data_dim = None
        with gzip.open(file_name, 'rt') as f:
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
                
    #        Read the gene info table

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
        
        return sd, si, ge
