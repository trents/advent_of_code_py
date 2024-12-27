## 2024 Problem 3: https://adventofcode.com/2024/day/3

import requests

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input3.txt')
text = response.text
print(text)