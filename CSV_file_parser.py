# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:23:35 2021

@author: tchan
"""

import csv

with open('1_lims_keys_to_file_map.csv') as csv_file:
    file = csv.reader(csv_file, delimiter = ',')
    count = 0
    for row in file:
        print(row[5],row[6],end=' ')
        if count == len(file)/2:
            print('\n',end=' ')
        count += 1
        