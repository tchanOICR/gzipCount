# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:45:41 2021

@author: tchan
"""

import gzip, sys

cycles = []
newCycles = []
totalCount = {'A':0,'T':0,'C':0,'G':0,'N':0}
maxLen = 0

for Input in sys.argv:
    if '.gz' not in Input:
        ()
    else:
        with gzip.open(Input,'rt') as current_file:
            line = 1
            for record in current_file:
                if 'R1.fastq' in Input:
                    count = 0
                elif 'R2.fastq' in Input and line == 2:
                    count = len(record)-1
                if line == 1 or line == 3:
                    line += 1
                elif line == 2:
                    testLen = len(record)-1
                    if testLen > maxLen:
                        if cycles == []:
                            for n in range(testLen*2):
                                cycles.append({'A':0,'T':0,'C':0,'G':0,'N':0})
                        else:
                            for n in range((testLen-maxLen)*2):
                                cycles.append({'A':0,'T':0,'C':0,'G':0,'N':0})
                        maxLen = testLen
                    for char in record[:-1]:
                        if char == 'A':
                            cycles[count]['A'] += 1
                            totalCount['A'] += 1
                        elif char == 'T':
                            cycles[count]['T'] += 1
                            totalCount['T'] += 1
                        elif char == 'C':
                            cycles[count]['C'] += 1
                            totalCount['C'] += 1
                        elif char == 'G':
                            cycles[count]['G'] += 1
                            totalCount['G'] += 1
                        elif char == 'N':
                            cycles[count]['N'] += 1
                            totalCount['N'] += 1
                        count += 1
                    line += 1
                elif line == 4:
                    line = 1
print(len(cycles))
for cycle in cycles:
    cycle = {key:val for key, val in cycle.items() if val != 0}
    newCycles.append(cycle)
print(newCycles)
print(totalCount)