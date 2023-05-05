# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:49:51 2023

@author: iceen
"""

import pandas as pd
import numpy as np
import glob
import os

"""In this file I will be converting the given accelerometer xyz values into expressed values of 'little g' by 
using the given ratio found by Dr. Gabriel Niculescu; (raw_acc - 512)/128. This will allow us to determine
the actual amount of gravity that the lemurs at any given moment which has been recorded."""

"""First however, we must make the raw data into a pandas dataframe in order to do this conversion."""

#pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\CSV_Files\Gisela1_2_3_4_5_6_7_with_Behavior.csv')  
source_dir = 'GN_CSV_files'
file_name = 'Gisela1_2_3_4_5_6_7_with_Behavior.csv'

filename = os.path.join(source_dir, file_name)

adf1 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Gisela1_2_3_4_5_6_7_with_Behavior.csv')
pd.options.display.max_columns = None
print('adf1:',adf1.info())
print('adf1:',adf1.head())

#time = adf1.Time
#timegroup = adf1.groupby(by="Time", sort=True)

#this will only call the X, Y, and Z columns
columns_x_y_z = adf1[['X', 'Y', 'Z']]
edited_x_y_z = (columns_x_y_z - 512)/128
adf1[['X','Y','Z']] = edited_x_y_z
#print(edited_x_y_z)
#print('adf1',adf1.head())
#adf1 is now edited and in forms of little g! Now to repeat for the rest of the files???
#the code below writes the updated dataframe into a NEW csv file.
os.makedirs(r'106 Data Sci\GN_CSV_Files\Converted_Data', exist_ok=True)
adf1.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela1_2_3_4_5_6_7_with_Behavior.csv',
            index=False)

#Start of file 2, just to make sure I'm converting correctly without breaking any of the working code
adf2 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Gisela8_9_10_11_12_13_14_15_16_with_Behavior.csv')
#print('adf2:', adf2.info())
#print('adf2',adf2.head())
edited_x_y_z_2 = (adf2[['X','Y','Z']] - 512)/128
adf2[['X', 'Y', 'Z']] = edited_x_y_z_2
adf2.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela8_9_10_11_12_13_14_15_16_with_Behavior.csv',
            index=False)

#Start of file 3, why not do them all separately to see what I can do in one line
adf3 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Gisela17_18_19_with_Behavior.csv')
adf3[['X','Y','Z']] = (adf3[['X','Y','Z']] - 512)/128
adf3.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela17_18_19_with_Behavior.csv',
            index=False)

#These can be pretty fast now! Only 3 lines total for files after the first. I'm not changing the second one however because
#it is interesting to see the evolution of the code, especially when removing irrelevant lines.
adf4 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Gisela21_22_24_with_Behavior.csv')
adf4[['X','Y','Z']] = (adf4[['X','Y','Z']] - 512)/128
adf4.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela21_22_24_with_Behavior.csv',
            index=False)

adf5 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Gisela26_27_28_with_Behavior.csv')
adf5[['X','Y','Z']] = (adf5[['X','Y','Z']] - 512)/128
adf5.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela26_27_28_with_Behavior.csv',
            index=False)

adf6 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Gisela29_30_with_Behavior.csv')
adf6[['X','Y','Z']] = (adf6[['X','Y','Z']] - 512)/128
adf6.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela29_30_with_Behavior.csv',
            index=False)

adf7 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Gisela32_with_Behavior.csv')
adf7[['X','Y','Z']] = (adf7[['X','Y','Z']] - 512)/128
adf7.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela32_with_Behavior.csv',
            index=False)




