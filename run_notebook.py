#!/usr/bin/env python 

import nbformat, fire 
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(path):
    """
    Run a Jupyter notebook and save the output.
    
    Args:
        path (str): Path to the notebook file.
    """
    with open(path) as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    
    ExecutePreprocessor(timeout=600, kernel_name='python3').preprocess(nb, {})
    print('done')

if __name__ == '__main__':
    fire.Fire(run_notebook)

    
