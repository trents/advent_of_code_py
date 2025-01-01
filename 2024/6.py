## 2024 Problem 6: https://adventofcode.com/2024/day/6

import requests

def find_cursor(maze):
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if maze[i][j] == "^" or maze[i][j] == ">" or maze[i][j] == "<" or maze[i][j] == "v":
                return i, j, maze[i][j]

# Change next 1-2 lines if you want to load input from different source

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input6.txt')
text = response.text

maze = text.split("\n")
print(find_cursor(maze))
