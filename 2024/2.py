## 2024 Problem 2: https://adventofcode.com/2024/day/2

import requests

def safety_checker(item):
## Each item must fulfill 2 conditions:
## 1: All adjacent pairs in item must be 1, 2, or 3 apart
## 2: All adjacent pairs in item must ascend or descend, no mixing

## Assume condition 1 is false until proven true
## Count the number of pairs that are 1, 2, or 3 apart, 
##  and if it's the total num of pairs, condition 1 is true

    condition1 = False
    values = item
    prior = values[0]
    count = 0
    size = len(values[1:])
    for number in values[1:]:
        if abs(int(number) - int(prior)) > 0 and abs(int(number) - int(prior)) < 4:
            count = count + 1
        prior = number
    if (count == size):
        condition1 = True

## Assume condition 2 is true until proven false
## If first pair is ascending, check pairs until one isn't ascending, which proves false
## If first pair is descending, check pairs until one isn't descending, which proves false

    condition2 = True
    progression = ""
    if int(values[0]) > int(values[1]):
        progression = "D"
    elif int(values[0]) < int(values[1]):
        progression = "I"
    else:
        condition2 = False

    prior = values[1]

    for number in values[2:]:
        if int(prior) == int(number):
            condition2 = False
        elif int(prior) > int(number) and progression == "I":
            condition2 = False
        elif int(prior) < int(number) and progression == "D":
            condition2 = False

        prior = number

    if condition1 and condition2:
        return 1
    else:
        return 0

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input2.txt')
text = response.text
list = text.split('\n')

total = 0

## For 2a, just safety_checker each item.

for item in list:
    total = total + safety_checker(item.split(" "))

print("Answer to 2024 Problem 2a:",total)

## For 2b, we need to safety check each item variation
## An item variation is one where one of the items in the line is missing

total = 0
for item in list:
    i = 0
    passed = 0
    numbers_in_item = item.split(" ")
    count_of_items = numbers_in_item.count
    for item in numbers_in_item:
        if(passed == 0):
            passed = safety_checker(numbers_in_item[:i] + numbers_in_item[i+1:])
        i = i + 1
    total = total + passed
print("Answer to 2024 Problem 2b:", total)