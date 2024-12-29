## 2024 Problem 4: https://adventofcode.com/2024/day/3

import requests
import re

def xmas_count(text):
    return text.count("XMAS") + text.count("SAMX")

def get_diagonal_strings(matrix):
    diagonals = []
    for i in range(len(matrix)):
        diagonal = ""
        for j in range(min(len(matrix[i]), len(matrix) - i)):
            diagonal += matrix[i + j][j]
        diagonals.append(diagonal)

    for j in range(1, len(matrix[0])):
        diagonal = ""
        for i in range(min(len(matrix), len(matrix[0]) - j)):
            diagonal += matrix[i][i + j]
        diagonals.append(diagonal)

    return diagonals

def transpose_list_of_strings(lst):
    max_len = max(len(s) for s in lst)
    result = []

    for i in range(max_len):
        row = []
        for s in lst:
            if i < len(s):
                row.append(s[i])
            else:
                row.append(" ")
        result.append("".join(row))

    return result


# Change next 1-2 lines if you want to load input from different source

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input4.txt')
text = response.text

text_list = text.split("\n")

total_xmas = 0

# Horizontal XMASes

for line in text_list:
    total_xmas += xmas_count(line)

# Vertical XMASes

transposed = transpose_list_of_strings(text_list)
for line in transposed:
    total_xmas += xmas_count(line)

# Diagonal XMASes

diagonals = get_diagonal_strings(text_list)
print(diagonals)
for line in diagonals:
    total_xmas += xmas_count(line)

diagonals = get_diagonal_strings(transposed)
for line in diagonals:
    total_xmas += xmas_count(line)

print(total_xmas)