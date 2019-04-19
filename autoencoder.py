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
