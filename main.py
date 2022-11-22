#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from itertools import combinations
from tqdm import tqdm

base = np.genfromtxt('input_matrix.csv', delimiter=';')
base = base.astype(int)

print(base)
def row_to_set_of_indexes(row):
    """
    generates sets of indexes with correct sum
    """
    a = []
    for r in range(len(row)-1):  # для всех размеров r комбинаций индексов
        for set in combinations(np.array(range(len(row)-1)),r+1): # перебор всех комбинаций индексов размером r
            if row[list(set)].sum() == row[len(row)-1]: #проверка суммы элементов
                a.append(list(set))
    return a

def index_to_row_with_zero(indexes, row): 
    
    """
    makes list of numbers (one row) and zeros of list of indexes and row
    """
    result_row = []
    j=0
    
    #return result_row
    for i in range(len(row)):
        if i in indexes:
            result_row.append(row[i])
        elif i == len(row)-1:
            result_row.append(row[i])
        else:
            result_row.append(0) 
    return result_row


row_sets = []
for i in range(len(base)-1):
    
    row_sets.append(row_to_set_of_indexes(base[i]))
rows_with_zeros = []
for i in range(len(base)-1):
    row_with_zeros = []
    for j in range(len(row_sets[i])):
        row_with_zeros.append(index_to_row_with_zero(row_sets[i][j], base[i]))
    rows_with_zeros.append(row_with_zeros)

import itertools

matrixes = []

for combo in tqdm(itertools.product(*rows_with_zeros)):
    matrixes.append(list(combo))


#print(np.array(matrixes))

for matrix in tqdm(range(len(matrixes))):
    if (np.sum(matrixes[matrix], axis=0)[:len(matrixes[matrix])] == base[len(base)-1][:len(matrixes[matrix])]).all():
        print()
        print(np.array(matrixes[matrix]))
        print(np.sum(matrixes[matrix], axis=0)[:len(matrixes[matrix])])
        break

            
            

print(len(matrixes))

input("Press enter to exit ;)")