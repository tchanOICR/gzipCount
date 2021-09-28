# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:45:41 2021

@author: tchan
"""

def file_reader(fileName,origFile):
    import gzip
    from datetime import datetime
    
    cycles = []
    maxLen = 0
    
    for Input in fileName:
        with gzip.open(Input,'rt') as current_file:
            line = 1
            for record in current_file:
                if line == 1 or line == 3:
                    line += 1
                elif line == 2:
                    if 'R1.fastq' in Input:
                        count = 0
                        origFile = str(Input)[:-11]
                    elif 'R2.fastq' in Input:
                        count = len(record)-1
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
        
            if 'R2.fastq' in Input:
                newCycles = []
                totalCount = {'A':0,'T':0,'C':0,'G':0,'N':0}
                
                for cycle in cycles:
                    if cycle == {'A':0,'T':0,'C':0,'G':0,'N':0}:
                        continue
                    cycle = {key:val for key, val in cycle.items() if val != 0}
                    newCycles.append(cycle)
                    for key in cycle:
                        totalCount[key] += cycle[key]
                
                textFile = open('/u/tchan/Sequence_Results/'+str(datetime.now().strftime('%d-%b-%Y_%H-%M-%S'))+'_'+origFile+'.txt','w')
                textFile.write(str(newCycles))
                textFile.write('\n'+str(totalCount))
                textFile.close()
                print('File created.')
                
                cycles = []
                maxLen = 0

def CSV_reader(fileName):
    import csv
    
    fastqFiles = []
    with open(fileName) as csv_file:
        file = csv.reader(csv_file, delimiter = ',')
        for row in file:
            if '.fastq.gz' in row[5] and '.fastq.gz' in row[6]:
                fastqFiles.append(row[5])
                fastqFiles.append(row[6])
    file_reader(fastqFiles,fileName)

def JSON_reader(fileName):
    import json
    
    fastqFiles = []
    with open(fileName) as json_file:
        data = json.loads(json_file.read())
        type(data)
        for list_value in data['results']:
            for key1 in list_value:
                if key1 == 'files':
                    for key2 in list_value['files']:
                        fastqFiles.append(key2['path'])
    file_reader(fastqFiles,fileName)

import sys

looseFiles = []
looseFileNames = []

for file_type in sys.argv:
    if '.fastq.gz' in file_type:
        looseFiles.append(file_type)
        looseFileNames.append(file_type)
    elif '.csv' in file_type:
        CSV_reader(file_type)
    elif '.json' in file_type:
        JSON_reader(file_type)
file_reader(looseFiles,looseFileNames)
