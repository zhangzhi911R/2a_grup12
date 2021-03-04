# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:35:02 2019

@author: PERSONAL
"""

import serial

def ambildata():
    ser = serial.Serial('COM6',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

ambildata()

import csv

def tuliscsv():
    ser = serial.Serial('COM6',9600)
    with open('uji.csv',mode='w') as csv_file:
        fieldnames = ['jarak']
        writer = csv.DictWriter(csv_file, fieldname=fieldnames)
        
        writer.writeheader()
        while(1):
            data = ser.readline().decode("utf-8").strip('\n').strip('r')
            writer.writerow({'jarak': data})

tuliscsv()