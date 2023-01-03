import numpy as np

file = "day_09_input.txt"

with open(file, "r") as f:
    lines = f.read().splitlines()
    f.close()

lines = [l.split(" ") for l in lines]
start = (1, 1)  # Row, Col


def move_head_one_step(direction, position):
    if direction == "U":
        new_position = (position[0] + 1, position[1])
    if direction == "D":
        new_position = (position[0] - 1, position[1])
    if direction == "L":
        new_position = (position[0], position[1] - 1)
    if direction == "R":
        new_position = (position[0], position[1] + 1)
    return new_position


def follow_head_one_step(position_tail, position_head):
    row = np.clip(position_head[0] - position_tail[0], -1, 1)
    col = np.clip(position_head[1] - position_tail[1], -1, 1)

    new_position_tail = (position_tail[0] + row, position_tail[1] + col)
    return new_position_tail


def check_adjacent(head, tail):
    row = head[0] - tail[0]
    col = head[1] - tail[1]

    if (abs(row) >= 2) | (abs(col) >= 2):
        adjacent = False
    else:
        adjacent = True

    return adjacent


def process_line(head, tail, line, verbose=False):
    visited = []
    direction = line[0]
    steps = int(line[1])

    for i in range(0, steps):
        head = move_head_one_step(direction=direction, position=head)
        adjacent = check_adjacent(head, tail)
        if not adjacent:
            tail = follow_head_one_step(tail, head)
        visited.append(tail)

    return head, tail, visited


head = start
tail = start
visited = []
verbose = False

for line in lines:
    head, tail, v = process_line(head, tail, line)
    visited += v

print(len(set(visited)))

# Part 2
# Now we need to simulate a full rope of length 10


def rope_follows_tail(head, rope):
    head_and_rope = [head] + rope
    for i in range(len(head_and_rope) - 1):
        a = head_and_rope[i]
        b = head_and_rope[i + 1]
        adjacent = check_adjacent(a, b)
        if not adjacent:
            new_b = follow_head_one_step(position_tail=b, position_head=a)
            head_and_rope[i + 1] = new_b

    new_rope = head_and_rope[1:]
    return head, new_rope


def process_line_rope(head, rope, line):
    visited = []
    direction = line[0]
    steps = int(line[1])

    for i in range(0, steps):
        head = move_head_one_step(direction=direction, position=head)
        head, rope = rope_follows_tail(head, rope)
        visited.append(rope[-1])

    return head, rope, visited


head = start
rope_length = 9  # +1 for the head
rope = [start] * rope_length
visited = []
verbose = False

for line in lines:
    head, rope, v = process_line_rope(head, rope, line)
    visited += v

print(len(set(visited)))
