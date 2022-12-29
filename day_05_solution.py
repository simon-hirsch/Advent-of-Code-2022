import numpy as np
from itertools import product

file = "day_05_input.txt"

with open(file, "r") as f:
    lines = f.read().splitlines()
    f.close()

stack = lines[: lines.index("")]
moves = lines[(lines.index("") + 1) :]
index = np.arange(1, 35, step=4, dtype=int)
parsed_stack = []

for i in index:
    this_stack = [stack[-s][i] for s in range(2, len(stack) + 1) if stack[-s][i] != " "]
    parsed_stack.append(this_stack)


def parse_move(move):
    split = move.split(" ")
    n = int(split[1])
    f = int(split[3])
    t = int(split[5])
    return n, f, t  # n, from, to,


def make_move(n, f, t, stack):
    stack = stack.copy()
    # Account for python indexing
    f = f - 1
    t = t - 1
    # Move crates
    for _ in range(0, n):
        crate_to_move = stack[f][-1]
        new_origination_stack = stack[f][:-1].copy()
        new_destination_stack = stack[t].copy() + [crate_to_move]
        stack[f] = new_origination_stack
        stack[t] = new_destination_stack
    return stack


part_1_stack = parsed_stack.copy()

for i, move in enumerate(moves):
    n, f, t = parse_move(move)
    part_1_stack = make_move(n, f, t, part_1_stack)

part_1_final_stack = part_1_stack.copy()
part_1_solution = "".join([i[-1] for i in part_1_final_stack])
part_1_solution

## Part 2


def make_move_CrateMover9001(n, f, t, stack):
    stack = stack.copy()
    # Account for python indexing
    f = f - 1
    t = t - 1
    # Move crates:
    crates_to_move = stack[f][-n:]
    new_origination_stack = stack[f][:-n].copy()
    new_destination_stack = stack[t].copy() + crates_to_move
    stack[f] = new_origination_stack
    stack[t] = new_destination_stack
    return stack


part_2_stack = parsed_stack.copy()

for i, move in enumerate(moves):
    n, f, t = parse_move(move)
    part_2_stack = make_move_CrateMover9001(n, f, t, part_2_stack)

part_2_final_stack = part_2_stack.copy()
part_2_solution = "".join([i[-1] for i in part_2_final_stack])
part_2_solution
