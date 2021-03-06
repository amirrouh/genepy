def read(link, data_dim):
    """
    This module downloads gene expression profile from NCBI GEO FTP website and parses it
    Parameters
    ----------
    link  : str
    This is the link to GEO soft_full.gz file on NCBI website
    data_dim  : int
    This gets number of genes needed to be considered ( data_dim = 10; only first 10 genes from the
    top of the input file will be considered in parsing data and data_dim = None means all the data)

    Returns
    -------
    dataset : numpy array
    dataset is a numpy array. Each row represents one cell gene expression data, the i_th column
    from the left shows the i_th gene expression values from the top in row input data table and
    the last column on the right shows the subset description type 0 being the first one showing 
    in the input file. 
    """
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


    '''
    #   Here, we create a temporary directory to store needed files
    ge.to_pickle('temp/ge')
    pickle.dump(sd , open( 'temp/sd', 'wb' ))
    pickle.dump(si , open( 'temp/si', 'wb' ))
    '''


    ge_array = np.array(ge)
    d = ge_array[:, 2:].astype(float)

    # Convert numpy array to training format for SVM solver
    data = []
    for i in range(len(d[0,:])):
        data.append(d[:data_dim,i])
    data = np.array(data)

    #   Assign numbers to subset types and make a target vector for classification
    labels = []
    for i in range(0, len(sd)):
        labels.append(len(si[i]) * [i])
    
    #   Merge the target groups (each type is a list in python, 
    #   this part merges the parts to have unit target vector)
    label_tmp = []
    for j in range(len(labels)):
        label_tmp += labels[j]
    labels = np.array(label_tmp)

    # dimension of input gene expression
    label_dimension = len(ge_array[0,2:])
    labels = labels.reshape((label_dimension,1))


    #   This line joins the data and labels as a new 2D array
    dataset = np.concatenate((data, labels), axis=1)

    #   This part randomly shuffles the data to be ready for training and testing purposes
    np.random.shuffle(dataset)

    # This file will be saved into temp folder in case of any need for review
    np.savetxt('temp/dataset.csv', dataset, fmt='%.3f', delimiter=',', newline='\n', header='')

    # This binary file will be save in the temp folder for faster load in other modules
    np.save('temp/dataset_binary', dataset)

    return dataset
