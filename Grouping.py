# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:28:03 2023

@author: iceen
"""
import numpy as np
import pandas as pd
import glob
import os

# =============================================================================
# my_files = glob.glob(os.path.join('C:\\Users\\iceen\\OneDrive\\Desktop\\106 Data Sci\\GN_CSV_Files\\Converted_Data\\dti', 'df*.csv'))
# for index, a_file in enumerate(my_files):
#     df = pd.read_csv(a_file)
#     df['']
#     df.to_csv(f'C:\\Users\\iceen\\OneDrive\\Desktop\\106 Data Sci\\GN_CSV_Files\\Converted_Data\\dti\\df{index}.csv', index = False)
# =============================================================================

df1 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\dti\df0.csv')
grouped = df1.groupby("dti")
agg = grouped.agg({"dti": ["mean", "std", "skew"]})
#df1.groupby('dti').apply(pd.DataFrame.kurt)
print(agg)