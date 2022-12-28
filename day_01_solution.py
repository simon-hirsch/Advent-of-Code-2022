import numpy as np

file = "day_01_input.txt"

with open(file, "r") as f:
    lines = f.read().splitlines()
    f.close()

splits = [i for i, line in enumerate(lines) if line == ""]

## Parse to simple array
array = np.array(lines, dtype=str)
array[splits] = np.NaN
array = array.astype(float)
array[splits] = 0
array

it = [0] + splits + [len(array)]
calories = np.empty(len(it))

for k, (i, j) in enumerate(zip(it, it[1:])):
    calories[k] = np.sum(array[i:j])

# Part 1
np.max(calories)
np.argmax(calories)

# Part 2
np.sum(np.sort(calories)[-3:])
