## 2024 Problem 3: https://adventofcode.com/2024/day/3

import requests
import re

def is_number(string):
    pattern = r"^-?\d+(\.\d+)?$"
    return bool(re.match(pattern, string))

# Change next 1-2 lines if you want to load input from different source

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input3.txt')
text = response.text

## Solution to 3a

# regex pattern to match function for day 3a
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

total = 0
matches = re.findall(pattern, text)

# for each valid function, add product of arguments to total

for match in matches:
    arguments = re.findall(r"\d{1,3}", match)
    total = total + int(arguments[0]) * int(arguments[1])

print("Answer to 2024 Problem 3a:",total)

# regex pattern to match 3 functions for day 3b
pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

is_do = True
total = 0

matches = re.findall(pattern,text)

# if do(), switch on
# if don't(), switch off
# if mul(#,#), add product of args to total

for match in matches:
    if match == "do()":
        is_do = True
    elif match == "don't()":
        is_do = False
    elif is_do and match.startswith("mul"):
        arguments = re.findall(r"\d{1,3}", match)
        total = total + int(arguments[0]) * int(arguments[1])

print("Answer to 2024 Problem 3b:",total)