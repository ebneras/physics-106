# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:08:20 2023

@author: iceen
"""

import pandas as pd
import numpy as np
import glob
import os
from datetime import datetime
from datetime import timedelta
time_parser = lambda x: pd.datetime.strptime(x, "%H,%M,%S.%f")
df1 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela1_2_3_4_5_6_7_with_Behavior.csv',
                  parse_dates=[['DATE', 'T']])
#ali = pd.to_datetime(df1['date_t'])
#print(ali.info())
#print(df1.info())
#print(df1.head())
#grins = input("wait")
df2 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela8_9_10_11_12_13_14_15_16_with_Behavior.csv',
                  parse_dates=[['DATE', 'T']])
df3 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela17_18_19_with_Behavior.csv',
                  parse_dates=[['DATE', 'T']])
df4 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela21_22_24_with_Behavior.csv',
                  parse_dates=[['DATE', 'T']])
df5 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela26_27_28_with_Behavior.csv',
                  parse_dates=[['DATE', 'T']])
df6 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela29_30_with_Behavior.csv',
                  parse_dates=[['DATE', 'T']])
df7 = pd.read_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela32_with_Behavior.csv',
                  parse_dates=[['DATE', 'T']])

# =============================================================================
# #mean accel, sqrt(ax^2+ay^2+az^2)
# Columnx = df1['X']
# Columny = df1['Y']
# Columnz = df1['Z']
# abs_accel = np.sqrt(Columnx**2+Columny**2+Columnz**2)
# print (abs_accel)
# df1['abs_accel'] = abs_accel
# df1.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela1_2_3_4_5_6_7_with_Behavior.csv',
#            index =False)
# # xmean = df1['X'].agg([np.sum, 'mean'])
# # print(xmean)
# Columnx = df2['X']
# Columny = df2['Y']
# Columnz = df2['Z']
# abs_accel = np.sqrt(Columnx**2+Columny**2+Columnz**2)
# print (abs_accel)
# df2['abs_accel'] = abs_accel
# df2.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela8_9_10_11_12_13_14_15_16_with_Behavior.csv',
#            index =False)
# 
# Columnx = df3['X']
# Columny = df3['Y']
# Columnz = df3['Z']
# abs_accel = np.sqrt(Columnx**2+Columny**2+Columnz**2)
# print (abs_accel)
# df3['abs_accel'] = abs_accel
# df3.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela17_18_19_with_Behavior.csv',
#            index =False)
# 
# Columnx = df4['X']
# Columny = df4['Y']
# Columnz = df4['Z']
# abs_accel = np.sqrt(Columnx**2+Columny**2+Columnz**2)
# print (abs_accel)
# df4['abs_accel'] = abs_accel
# df4.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela21_22_24_with_Behavior.csv',
#            index =False)
# 
# Columnx = df5['X']
# Columny = df5['Y']
# Columnz = df5['Z']
# abs_accel = np.sqrt(Columnx**2+Columny**2+Columnz**2)
# print (abs_accel)
# df5['abs_accel'] = abs_accel
# df5.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela26_27_28_with_Behavior.csv',
#            index =False)
# 
# Columnx = df6['X']
# Columny = df6['Y']
# Columnz = df6['Z']
# abs_accel = np.sqrt(Columnx**2+Columny**2+Columnz**2)
# print (abs_accel)
# df6['abs_accel'] = abs_accel
# df6.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela29_30_with_Behavior.csv',
#            index =False)
# 
# Columnx = df7['X']
# Columny = df7['X']
# Columnz = df7['Z']
# abs_accel = np.sqrt(Columnx**2+Columny**2+Columnz**2)
# print (abs_accel)
# df7['abs_accel'] = abs_accel
# df7.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela32_with_Behavior.csv',
#            index =False)
# 
# #delta t operation
# t_start = df1['DATE_T'].iloc[0]
# df1['dt']=(df1['DATE_T']-t_start).astype('timedelta64[ns]')/np.timedelta64(1, 's')
# df1.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela1_2_3_4_5_6_7_with_Behavior.csv',
#            index=False)
# t_start = df2['DATE_T'].iloc[0]
# df2['dt']=(df2['DATE_T']-t_start).astype('timedelta64[ns]')/np.timedelta64(1, 's')
# df2.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela8_9_10_11_12_13_14_15_16_with_Behavior.csv',
#            index=False)
# t_start = df3['DATE_T'].iloc[0]
# df3['dt']=(df3['DATE_T']-t_start).astype('timedelta64[ns]')/np.timedelta64(1, 's')
# df3.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela17_18_19_with_Behavior.csv',
#            index=False)
# t_start = df4['DATE_T'].iloc[0]
# df4['dt']=(df4['DATE_T']-t_start).astype('timedelta64[ns]')/np.timedelta64(1, 's')
# df4.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela21_22_24_with_Behavior.csv',
#            index=False)
# t_start = df5['DATE_T'].iloc[0]
# df5['dt']=(df5['DATE_T']-t_start).astype('timedelta64[ns]')/np.timedelta64(1, 's')
# df5.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela26_27_28_with_Behavior.csv',
#            index=False)
# t_start = df6['DATE_T'].iloc[0]
# df6['dt']=(df6['DATE_T']-t_start).astype('timedelta64[ns]')/np.timedelta64(1, 's')
# df6.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela29_30_with_Behavior.csv',
#            index=False)
# t_start = df7['DATE_T'].iloc[0]
# df7['dt']=(df7['DATE_T']-t_start).astype('timedelta64[ns]')/np.timedelta64(1, 's')
# df7.to_csv(r'C:\Users\iceen\OneDrive\Desktop\106 Data Sci\GN_CSV_Files\Converted_Data\Gisela32_with_Behavior.csv', 
#            index=False)
# =============================================================================
#come back to this later to try and prevent from having to call each and every dataframe individually
#with a new line of code for each dataframe
# def df(DataFrame):
#     print(CONTEXT, "\n", BEHAVIOR)


cols = df1.columns
for acol in cols:
    if "Unamed" in acol:
        df1.drop(acol, axis=1)

"""In order to take the mean, std, etc., for abs accel, first you should figure out how to parse the time data 
into groups. This way you can actual take the mean for the range that you set for time, aim for 0.5 seconds.
Not entirely sure where or how to start on that but it will be figured out eventually."""


grouped = df1.groupby("CONTEXT")
agg = grouped.agg({"abs_accel": ["mean", "std", "skew"]})
print("\n1",agg)
grouped = df2.groupby("CONTEXT")
agg = grouped.agg({"abs_accel": ["mean", "std", "skew"]})
print("\n2",agg)
grouped = df3.groupby("CONTEXT")
agg = grouped.agg({"abs_accel": ["mean", "std", "skew"]})
print("\n3",agg)
grouped = df4.groupby("CONTEXT")
agg = grouped.agg({"abs_accel": ["mean", "std", "skew"]})
print("\n4",agg)
grouped = df5.groupby("CONTEXT")
agg = grouped.agg({"abs_accel": ["mean", "std", "skew"]})
print("\n5",agg)
grouped = df6.groupby("CONTEXT")
agg = grouped.agg({"abs_accel": ["mean", "std", "skew"]})
print("\n6",agg)
grouped = df7.groupby("CONTEXT")
agg = grouped.agg({"abs_accel": ["mean", "std", "skew"]})
print("\n7",agg)