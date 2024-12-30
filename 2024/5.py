## 2024 Problem 5: https://adventofcode.com/2024/day/5

import requests
import re
from itertools import permutations

def check_order(order, rules):
    """
    This function splits the rules list, then checks each pair of orders to see if it's a valid rule.
    If all are valid, return True; if not, return False
    """
    rule_prev = []
    rule_next = []
    for rule in rules:
        pair = rule.split("|")
        rule_prev.append(pair[0])
        rule_next.append(pair[1])

    order_list = order.split(",")
    
    i = 0
    true_count = 0
    while i < len(order_list) - 1:
        j = 0
        while j < len(rule_prev):
            if rule_prev[j] == order_list[i] and rule_next[j] == order_list[i + 1]:
                true_count += 1
            j = j + 1
        i = i + 1

    if true_count == len(order_list) - 1:
        return True
    else:
        return False
    
def valid_rule(first_value, second_value, rules):
    """
    Check if there's a valid rule for the first and second value
    """

    rule_prev = []
    rule_next = []
    for rule in rules:
        pair = rule.split("|")
        rule_prev.append(pair[0])
        rule_next.append(pair[1])

    j = 0
    while j < len(rule_prev):
        if rule_prev[j] == first_value and rule_next[j] == second_value:
            return True
        j = j + 1
    return False

def insertion_sort(order, rules):
    """
    Perform insertion sort on order according to the rules list
    """

    order_list = order.split(",")
    
    n = len(order_list)

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = order_list[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and valid_rule(key, order_list[j], rules):  # Move elements greater than key one position ahead
            order_list[j+1] = order_list[j]  # Shift elements to the right
            j -= 1
        order_list[j+1] = key  # Insert the key in the correct position

    new_order = ','.join([str(x) for x in order_list])

    return new_order

# Change next 1-2 lines if you want to load input from different source

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input5.txt')
text = response.text

rules_list, orders_list = text.split("\n\n")
rules = rules_list.split("\n")
orders = orders_list.split("\n")

total = 0

# Sum the middle value of the valid order lists

for order in orders:
    if check_order(order, rules):
        items = order.split(",")
        total += int(items[len(items) // 2])

print("Answer to 2024 Problem 5a:",total)

total = 0

# For the invalid lists, sort them, then sum the middle values

for order in orders:
    if not check_order(order, rules):
        sorted_order = insertion_sort(order, rules)
        items = sorted_order.split(",")
        total += int(items[len(items) // 2])

print("Answer to 2024 Problem 5b:",total)