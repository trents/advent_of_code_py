## 2024 Problem 6: https://adventofcode.com/2024/day/6

import requests

def find_cursor(maze):
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if maze[i][j] == "^" or maze[i][j] == ">" or maze[i][j] == "<" or maze[i][j] == "v":
                return i, j, maze[i][j]
            
def get_x_coordinates(maze):
    coords_list = []
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if maze[i][j] == "X":
                coords_list.append([i,j])
    return coords_list

def move_cursor(maze):
    xloc, yloc, cursor_shape = find_cursor(maze)

    if cursor_shape == "^":
        if xloc == 0:
            maze[xloc][yloc] = "X"
            return maze, "E"
        elif maze[xloc-1][yloc] == "#":
            maze[xloc][yloc] = ">"
            return maze, "N"
        else:
            maze[xloc][yloc] = "X"
            maze[xloc-1][yloc] = "^"
            return maze, "N"
    elif cursor_shape == ">":
        if yloc == len(maze[0]) - 1:
            maze[xloc][yloc] = "X"
            return maze, "E"
        elif maze[xloc][yloc+1] == "#":
            maze[xloc][yloc] = "v"
            return maze, "N"
        else:
            maze[xloc][yloc] = "X"
            maze[xloc][yloc+1] = ">"
            return maze, "N"
    elif cursor_shape == "v":
        if yloc == len(maze) - 1:
            maze[xloc][yloc] = "X"
            return maze, "E"
        elif maze[xloc+1][yloc] == "#":
            maze[xloc][yloc] = "<"
            return maze, "N"
        else:
            maze[xloc][yloc] = "X"
            maze[xloc+1][yloc] = "v"
            return maze, "N"
    elif cursor_shape == "<":
        if yloc == 0:
            maze[xloc][yloc] = "X"
            return maze, "E"
        elif maze[xloc][yloc-1] == "#":
            maze[xloc][yloc] = "^"
            return maze, "N"
        else:
            maze[xloc][yloc] = "X"
            maze[xloc][yloc-1] = "<"
            return maze, "N"

def count_xs(maze):
    x_count = 0
    for line in maze:
        for char in line:
            if char == "X":
                x_count += 1
    return x_count

def reset_maze(maze):
    maze_lines = text.split("\n")
    maze = []
    for line in maze_lines:
        line_chars = [char for char in line]
        maze.append(line_chars)
    return maze

# Change next 1-2 lines if you want to load input from different source

response = requests.get('https://raw.githubusercontent.com/trents/advent_of_code_py/refs/heads/main/2024/input6.txt')
text = response.text

maze_lines = text.split("\n")
maze = []
for line in maze_lines:
    line_chars = [char for char in line]
    maze.append(line_chars)

exit_value = "N"
while exit_value == "N":
    maze, exit_value = move_cursor(maze)

print("Solution to 2024 Problem 6a:",count_xs(maze))

print("Solution to 2024 Problem 6b:",loop_count)
