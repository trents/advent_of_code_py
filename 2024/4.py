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

def get_3x3_grids(array_of_strings):
    if len(array_of_strings) < 3 or any(len(row) < 3 for row in array_of_strings):
        return []

    grids = []
    for i in range(len(array_of_strings) - 2):
        for j in range(len(array_of_strings[0]) - 2):
            grid = [row[j:j+3] for row in array_of_strings[i:i+3]]
            grids.append(grid)
    return grids

def mas_cross(grid):
    if len(grid) != 3:
        return False
    else:
        if grid[1][1] == "A" and ((grid[0][2] == "M" and grid[2][0] == "S" and grid[0][0] == "M" and grid[2][2] == "S") or (grid[0][2] == "M" and grid[2][0] == "S" and grid[0][0] == "S" and grid[2][2] == "M") or (grid[0][2] == "S" and grid[2][0] == "M" and grid[0][0] == "M" and grid[2][2] == "S") or (grid[0][2] == "S" and grid[2][0] == "M" and grid[0][0] == "S" and grid[2][2] == "M")):
            return True
        else:
            return False
        
# Change next 1-2 lines if you want to load input from different source

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input4.txt')
text = response.text

text_list = text.split("\n")

total_xmas = 0

# Horizontal XMASes

for line in text_list:
    total_xmas += xmas_count(line)

# Vertical XMASes

rotated = [''.join(row[i] for row in text_list[::-1]) for i in range(len(text_list[0]))]

for line in rotated:
    total_xmas += xmas_count(line)

# Diagonal XMASes

diagonals = get_diagonal_strings(text_list)
for line in diagonals:
    total_xmas += xmas_count(line)

other_diagonals = get_diagonal_strings(rotated)
for line in other_diagonals:
    total_xmas += xmas_count(line)

print("Answer to 2024 Problem 4a:",total_xmas)

grids = get_3x3_grids(text_list)

count_of_mas_crosses = 0
for grid in grids:
    if mas_cross(grid):
        count_of_mas_crosses += 1

print("Answer to 2024 Problem 4b:",count_of_mas_crosses)