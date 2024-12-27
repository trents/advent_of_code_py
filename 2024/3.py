## 2024 Problem 3: https://adventofcode.com/2024/day/3

import requests
import re

def is_number(string):
    pattern = r"^-?\d+(\.\d+)?$"
    return bool(re.match(pattern, string))

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input3.txt')
text = response.text

# regex pattern to match function
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

total = 0
matches = re.findall(pattern, text)

for match in matches:
    arguments = re.findall(r"\d{1,3}", match)
    total = total + int(arguments[0]) * int(arguments[1])

print("Answer to 2024 Problem 3a:",total)
