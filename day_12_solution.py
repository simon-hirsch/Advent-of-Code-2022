import numpy as np
import copy
from scipy import sparse

file = "day_12_input.txt"
#file = "day_12_input_test.txt"

with open(file) as f:
    lines = f.readlines()
    f.close()

lines_letters = [l.replace("\n", "") for l in lines]
lines_elevation = [
    [ord(x) % 32 if x not in ["S", "E"] else 0 for x in l] for l in lines_letters
]

elevation = np.stack([np.array([*l], dtype=int) for l in lines_elevation], axis=1)
letters = np.stack([np.array([*l], dtype=str) for l in lines_letters], axis=1)

elevation = elevation.T
letters = letters.T

start = tuple(np.argwhere(letters == "S")[0])
end = tuple(np.argwhere(letters == "E")[0])

elevation[letters == "E"] = 26
elevation[letters == "S"] = 0
directions = ["u", "d", "l", "r"]

width = elevation.shape[1]
length = elevation.shape[0]

global directions
global elevation
global width
global length


def next_location(state, direction):
    if direction == "u":
        new = (state[0] - 1, state[1])
    if direction == "d":
        new = (state[0] + 1, state[1])
    if direction == "l":
        new = (state[0], state[1] - 1)
    if direction == "r":
        new = (state[0], state[1] + 1)
    return new

def is_in_map(state):
    max_x = elevation.shape[0]
    max_y = elevation.shape[1]
    x_valid = (state[0] >= 0) & (state[0] < max_x)
    y_valid = (state[1] >= 0) & (state[1] < max_y)
    return x_valid & y_valid


def is_possible(state, new):
    return elevation[new] - elevation[state] <= 1


def get_adjacent(state):
    adjacent = []
    for direction in directions:
        new = next_location(state, direction)
        if is_in_map(new):
            if is_possible(state, new):
                adjacent.append(new)
    return adjacent


def idx(position):
    return position[0] * width + position[1]

n = elevation.shape[0] * elevation.shape[1]
A = np.zeros((n, n), dtype=int)

for i in range(length):
    for j in range(width):
        adjacent = get_adjacent((i, j))
        for a in adjacent:
            A[idx((i, j)), idx(a)] = 1

B = A.copy()
A @ A
AA = sparse.csr_matrix(A)
BB = sparse.csr_matrix(B)

## test solution works
## Normal solution does not 
## why?
## https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-12-with-python/

steps = 1
while BB.toarray()[idx(start), idx(end)] == 0 and steps < 1000:
    BB = BB @ AA
    steps += 1
    if steps % 50 == 0 : 
        print(steps)



steps




start

def already_visited(state, seen):
    return state in seen


def prune_adjacent(nodes, seen):
    return [n for n in nodes if not already_visited(n, seen)]


node = copy.copy(start)
seen = []
queue = []
traversed = []

seen.append(node)
queue.append(node)

counter = 0

while len(queue) > 0:
    found = False
    node = queue.pop(0)
    adjacent_nodes = get_adjacent(node)
    for adj_node in adjacent_nodes:
        if adj_node == end:
            found = True
            print(counter, "found", adj_node, end)
            break
        if not already_visited(adj_node, seen):
            traversed.append(adj_node)
            seen.append(adj_node)
            queue.append(adj_node)
    if found:
        break
    else:
        counter += 1
    print(counter, node, queue)

counter

len(set(seen))

queue.pop(1)

len(traversed)
