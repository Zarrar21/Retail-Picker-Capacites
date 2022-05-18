# -*- coding: utf-8 -*-
"""Retail Capacities Solution 3 v3.0 12AM Structure .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WXkdt-NGTjiwokLaMsL4fSBj4j2uKGDX
"""

# in majority cases, solution 3 would more evenly divide capacities across the 9 shifts as compared to solution 1 and 2.

bearable_change = int(input('Enter Bearable Change Value '))
type(bearable_change)

import pandas as pd
import numpy as np

df = pd.read_csv('/content/Target Requirements Data - 16-05-2022.csv')
df = df.dropna()
date_list = df.Date.unique().tolist()
warehouse_list = df.Warehouse.unique().tolist()
hour_list = df.Hour.unique().tolist()
df.head()

final_df = pd.DataFrame(columns = ['Warehouse', 'Date', 'Shift_Start', 'Set Capacity'])

for date in date_list:
  date_df = df[df['Date'] == date]
  for warehouse in warehouse_list:
    daily_ew_df = date_df[date_df.Warehouse == warehouse]

    for hour in range(8,12):
      hourly_df = daily_ew_df[daily_ew_df.Hour == hour]

      if (hourly_df.empty == True):
        final_df = final_df.append({'Warehouse' : warehouse, 'Date' : date, 'Shift_Start' : hour
                                    , 'Set Capacity' : 0}, ignore_index = True)
      elif (hour == 8):
        final_df = final_df.append({'Warehouse' : warehouse, 'Date' : date, 'Shift_Start' : hour
                                    , 'Set Capacity' : hourly_df.Requirement.values[0]}, ignore_index = True)
      elif ((hour > 8 and hour  <= 11) and (hourly_df.Requirement.values[0] <= final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (final_df['Shift_Start'] < hour)]['Set Capacity'].sum() + bearable_change)):
        final_df = final_df.append({'Warehouse' : warehouse, 'Date' : date, 'Shift_Start' : hour
                                    , 'Set Capacity' : 0}, ignore_index = True)
      else:
        final_df = final_df.append({'Warehouse' : warehouse, 'Date' : date, 'Shift_Start' : hour
                                    , 'Set Capacity' : (hourly_df.Requirement.values[0] - final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (final_df['Shift_Start'] < hour)]['Set Capacity'].sum())}, ignore_index = True)
      
    for hour in range(23,19,-1):
      hourly_df = daily_ew_df[daily_ew_df.Hour == hour]
      if (hourly_df.empty == True):
        final_df = final_df.append({'Warehouse' : warehouse, 'Date' : date, 'Shift_Start' : hour - 7
                                    , 'Set Capacity' : 0}, ignore_index = True)
      elif (hour == 23):
        final_df = final_df.append({'Warehouse' : hourly_df.Warehouse.values[0], 'Date' : hourly_df.Date.values[0], 'Shift_Start' : hour - 7
                                    , 'Set Capacity' : hourly_df.Requirement.values[0]}, ignore_index = True)
      elif ((hour < 23 and hour  >= 20) and (hourly_df.Requirement.values[0] <= final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (final_df['Shift_Start'] > (hour - 7) )]['Set Capacity'].sum() + bearable_change)):
        final_df = final_df.append({'Warehouse' : hourly_df.Warehouse.values[0], 'Date' : hourly_df.Date.values[0], 'Shift_Start' : hour - 7
                                    , 'Set Capacity' : 0}, ignore_index = True)
      else:
        final_df = final_df.append({'Warehouse' : hourly_df.Warehouse.values[0], 'Date' : hourly_df.Date.values[0], 'Shift_Start' : hour - 7
                                    , 'Set Capacity' : (hourly_df.Requirement.values[0] - final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (final_df['Shift_Start'] > (hour - 7) )]['Set Capacity'].sum())}, ignore_index = True)


    hour12_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (final_df['Shift_Start'] >= 8) & (final_df['Shift_Start'] <= 11)]['Set Capacity'].sum())
    hour13_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (((final_df['Shift_Start'] >= 8) & (final_df['Shift_Start'] <= 11)) | (final_df['Shift_Start'] == 13))]['Set Capacity'].sum())
    hour14_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (((final_df['Shift_Start'] >= 8) & (final_df['Shift_Start'] <= 11)) | ((final_df['Shift_Start'] >= 13) & (final_df['Shift_Start'] <= 14)))]['Set Capacity'].sum())
    hour15_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (((final_df['Shift_Start'] >= 8) & (final_df['Shift_Start'] <= 11)) | ((final_df['Shift_Start'] >= 13) & (final_df['Shift_Start'] <= 15)))]['Set Capacity'].sum())
    hour16_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (((final_df['Shift_Start'] >= 9) & (final_df['Shift_Start'] <= 11)) | ((final_df['Shift_Start'] >= 13) & (final_df['Shift_Start'] <= 16)))]['Set Capacity'].sum())
    hour17_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & (((final_df['Shift_Start'] >= 10) & (final_df['Shift_Start'] <= 11)) | ((final_df['Shift_Start'] >= 13) & (final_df['Shift_Start'] <= 16)))]['Set Capacity'].sum())
    hour18_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & ((final_df['Shift_Start'] == 11) | ((final_df['Shift_Start'] >= 13) & (final_df['Shift_Start'] <= 16)))]['Set Capacity'].sum())
    hour19_availability = (final_df.loc[ (final_df['Date'] == date) & (final_df['Warehouse'] == warehouse) & ((final_df['Shift_Start'] >= 13) & (final_df['Shift_Start'] <= 16))]['Set Capacity'].sum())
    
    availability_list = [hour12_availability, hour13_availability, hour14_availability, hour15_availability, hour16_availability, hour17_availability, hour18_availability, hour19_availability]
    
    if (daily_ew_df[daily_ew_df.Hour == 12].empty == True):
      hour12_req = 0
    else:
      hour12_req = daily_ew_df[daily_ew_df.Hour == 12].Requirement.values[0]
    
    if (daily_ew_df[daily_ew_df.Hour == 13].empty == True):
      hour13_req = 0
    else:
      hour13_req = daily_ew_df[daily_ew_df.Hour == 13].Requirement.values[0]
    
    if (daily_ew_df[daily_ew_df.Hour == 14].empty == True):
      hour14_req = 0
    else:
      hour14_req = daily_ew_df[daily_ew_df.Hour == 14].Requirement.values[0]

    if (daily_ew_df[daily_ew_df.Hour == 15].empty == True):
      hour15_req = 0
    else:
      hour15_req = daily_ew_df[daily_ew_df.Hour == 15].Requirement.values[0]
    
    if (daily_ew_df[daily_ew_df.Hour == 16].empty == True):
      hour16_req = 0
    else:
      hour16_req = daily_ew_df[daily_ew_df.Hour == 16].Requirement.values[0]
    
    if (daily_ew_df[daily_ew_df.Hour == 17].empty == True):
      hour17_req = 0
    else:
      hour17_req = daily_ew_df[daily_ew_df.Hour == 17].Requirement.values[0]
    
    if (daily_ew_df[daily_ew_df.Hour == 18].empty == True):
      hour18_req = 0
    else:
      hour18_req = daily_ew_df[daily_ew_df.Hour == 18].Requirement.values[0]
    
    if (daily_ew_df[daily_ew_df.Hour == 19].empty == True):
      hour19_req = 0
    else:
      hour19_req = daily_ew_df[daily_ew_df.Hour == 19].Requirement.values[0]

    # hour13_req = daily_ew_df[daily_ew_df.Hour == 13].Requirement.values[0]
    # hour14_req = daily_ew_df[daily_ew_df.Hour == 14].Requirement.values[0]
    # hour15_req = daily_ew_df[daily_ew_df.Hour == 15].Requirement.values[0]
    # hour16_req = daily_ew_df[daily_ew_df.Hour == 16].Requirement.values[0]
    # hour17_req = daily_ew_df[daily_ew_df.Hour == 17].Requirement.values[0]
    # hour18_req = daily_ew_df[daily_ew_df.Hour == 18].Requirement.values[0]
    # hour19_req = daily_ew_df[daily_ew_df.Hour == 19].Requirement.values[0]

    req_list = [hour12_req, hour13_req, hour14_req, hour15_req, hour16_req, hour17_req, hour18_req, hour19_req]

    capacity_adjustment = np.subtract(req_list,availability_list)
    
    if np.amax(capacity_adjustment) <= bearable_change:
      final_df = final_df.append({'Warehouse' : warehouse, 'Date' : date, 'Shift_Start' : 12
                                    , 'Set Capacity' : 0}, ignore_index = True)
    else:
      final_df = final_df.append({'Warehouse' : warehouse, 'Date' : date, 'Shift_Start' : 12
                                    , 'Set Capacity' : np.amax(capacity_adjustment)}, ignore_index = True)

final_df.head()

#shifting dataframe to csv
final_df.to_csv('/content/Picker Shifts raw format b1 - 16-05-2022 Week.csv', index = False)