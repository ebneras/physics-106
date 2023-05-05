# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:08:14 2023

@author: iceen
"""

import numpy as np
import pandas as pd
import matplotlib.pylot as plt
import os

from collections import counter
from pandas.plotting import scatter_matrix
import pickle

def get_train_test_data(args):
    f1,f2 = args
    df1 = pd.read_csv(f1)
    df2 = pd.read_csv(f2)
    print(df1.info())
    print(df2.info())
    print('Retrieving train/test data')
    return (df1,df2)

file1 = os.path.join()