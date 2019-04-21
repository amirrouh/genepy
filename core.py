import shutil
'''
This module handles more general functions such as loggin the solution
'''

def log(entry):
    '''
    This function logs epecific event to a file 'log.txt'

    Parameters
    -----

    Returns
    -----

    '''
    with open('temp/log.txt', 'a') as file:
        file.writelines(entry + '\n')


def clean():
    '''
    This function cleans the temp folder from last run

    Parameters
    -----

    Returns
    -----

    '''
    try:
        shutil.rmtree('temp')
    except OSError:
        pass