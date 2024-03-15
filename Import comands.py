#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:23:05 2024

@author: andrewgiannettino
"""
import os
os.listdir()
import csv
path='/Users/andrewgiannettino/Downloads/contacts.csv'
with open (path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")
    
    for row in csvreader:
        if row[2] =='125-890-6291':
        print(row[0])
        
        