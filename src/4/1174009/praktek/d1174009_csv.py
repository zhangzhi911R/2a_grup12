# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:36:46 2019

@author: Dwi
"""
#no1
import csv

with open('coba.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Kolom nya adalah {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} kerja di {row[1]} lahir pada bulan {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')

#no2
import csv

with open('coba.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'kolom nya adalah {", ".join(row)}')
            line_count += 1
        print(f'\t{row["nama"]} kerja di {row["kerjaan"]} department, dan lahir pada bulan {row["bulan"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
def bacacsvlist():
    with open('coba.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f' {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t Orang Ini {row[0]} \ {row[1]} lahir {row[2]}.')
                line_count += 1    
    
    
def nulis():
    with open('test-tulis.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Ucok', 'Tukang', 'November'])
        employee_writer.writerow(['Udin', 'Mandor', 'April'])
    
    


