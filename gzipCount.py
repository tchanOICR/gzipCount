# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:45:41 2021

@author: tchan
"""

def file_reader(fileName):
    import gzip

    cycles = []

    for Input in fileName:
        with gzip.open(Input,'rt') as current_file:
            line = 1
            
            for record in current_file:
                record = record.rstrip()
                
                if line == 1 or line == 3:
                    line += 1
                    
                elif line == 2:
                    if 'R1.fastq' in Input:
                        count = 0
                    elif 'R2.fastq' in Input:
                        count = len(record)
                        
                    if cycles == []:
                        for n in range(len(record)*2):
                            cycles.append({'A':0,'T':0,'C':0,'G':0,'N':0})

                    for char in record:
                        cycles[count][char] += 1
                        count += 1

                    line += 1
                elif line == 4:
                    line = 1

            if 'R2.fastq' in Input:
                totalCount = {'A':0,'T':0,'C':0,'G':0,'N':0}

                for cycle in cycles:
                    for key in cycle:
                        totalCount[key] += cycle[key]              
                print(str(cycles)+'\n'+str(totalCount), file = sys.stdout)

                cycles = []

import sys

looseFiles = []

for file_type in sys.argv:
    if '.fastq.gz' in file_type:
        looseFiles.append(file_type)
file_reader(looseFiles)