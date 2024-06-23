import random

# Define the maze
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the start and end points
start = (1, 1)
end = (8, 8)

# Solve the maze using a random walk
current_position = start
path = [current_position]
while current_position!= end:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)
    for direction in directions:
        new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if (0 <= new_position[0] < len(maze)) and (0 <= new_position[1] < len(maze[0])) and (maze[new_position[0]][new_position[1]] == 0):
            current_position = new_position
            path.append(current_position)
            break

# Print the path
print("The path is:")
for position in path:
    print(position)