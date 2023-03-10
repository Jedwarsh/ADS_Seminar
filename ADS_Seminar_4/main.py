from collections import deque
import numpy as np


def find_distances(matrix):
    queue = deque()
    distances = [[float('inf') for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                queue.append((i, j))
                distances[i][j] = 0

    while queue:
        curr_i, curr_j = queue.popleft()

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_i, neighbor_j = curr_i + di, curr_j + dj
            if (
                0 <= neighbor_i < len(matrix) and
                0 <= neighbor_j < len(matrix[0]) and
                matrix[neighbor_i][neighbor_j] != 'S' and
                distances[neighbor_i][neighbor_j] == float('inf')
            ):
                distances[neighbor_i][neighbor_j] = distances[curr_i][curr_j] + 1
                queue.append((neighbor_i, neighbor_j))

    return distances


def max_value_position(matrix):
    position_of_maxes = []
    maxes = np.amax(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == maxes:
                position_of_maxes.append([i, j])
    return position_of_maxes


matrix_for_city1 = [[0, 0, 0, "S", 0], [0, 0, 0, 0, 0], [0, "S", 0, 0, 0], [0, 0, 0, 0, 0], ["S", 0, 0, 0, 0],
                    [0, 0, "S", 0, "S"]]
matrix_for_city2 = [[0, 0, 0, 0], [0, "S", 0, 0], [0, 0, 0, "S"], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                    ["S", 0, 0, 0], [0, 0, 0, "S"], [0, "S", 0, 0], [0, 0, 0, 0]]
matrix_for_city3 = [[0, 0, 0, 0], [0, "S", 0, 0], [0, 0, 0, "S"], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                    [0, 0, 0, 0], ["S", 0, 0, 0], [0, 0, 0, "S"], [0, "S", 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                    [0, 0, 0, 0], [0, 0, 0, 0], [0, "S", 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

matrix_for_city = find_distances(matrix_for_city3)
for k in range(len(matrix_for_city)):
    print(matrix_for_city[k])

positions = max_value_position(matrix_for_city)
for k in range(len(positions)):
    print(positions[k])

