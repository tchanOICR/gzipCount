# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:04:50 2021

@author: tchan
"""

import json, gzip

cycles = []
newCycles = []
foundFiles = []
totalCount = {'A':0,'T':0,'C':0,'G':0,'N':0}
maxLen = 0

with open('PASS01_fastq.json') as json_file:
    data = json.loads(json_file.read())
    type(data)
    for list_value in data['results']:
        for key1 in list_value:
            if key1 == 'files':
                for key2 in list_value['files']:
                    foundFiles.append(key2['path'])

for Input in foundFiles:
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
                    elif char == 'T':
                        cycles[count]['T'] += 1
                    elif char == 'C':
                        cycles[count]['C'] += 1
                    elif char == 'G':
                        cycles[count]['G'] += 1
                    elif char == 'N':
                        cycles[count]['N'] += 1
                    count += 1
                line += 1
            elif line == 4:
                line = 1
for cycle in cycles:
    cycle = {key:val for key, val in cycle.items() if val != 0}
    newCycles.append(cycle)
    for key in cycle:
        totalCount[key] += cycle[key]
#print(newCycles)
print(totalCount)