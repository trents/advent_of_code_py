import numpy as np
import pandas as pd

## 2024 Problem 1: https://adventofcode.com/2024/day/1

## If using this code, change the below URL to the location of your input file
## I preprocessed into a comma-delimited format with col1 and col2 as headers

df = pd.read_csv('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input1.txt', delimiter=',') 

## 1a: Sort each column by value, get the pairwise absolute difference between
## the sorted columns, then return the sum of those differences

col1 = df['col1'].sort_values().reset_index(drop=True)
col2 = df['col2'].sort_values().reset_index(drop=True)

df2 = abs(col1 - col2)
print("Answer to 2024 Problem 1a:", df2.sum())

## 1b: Get the value count of col2, then multiply each value in col1 by the count of
## that value in col2, then return the sum of those products

col2_pivot = col2.value_counts()
col2_pivot.columns = ['Value', 'Count']

total = 0
for x in col1:
    if x in col2_pivot:
        total = total + x * col2_pivot.at[x]

print("Answer to 2024 Problem 1b:", total)