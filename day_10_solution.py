# Solution Day 10
import numpy as np
import pandas as pd
from itertools import product


file = "day_10_input.txt"

with open(file, "r") as f:
    lines = f.read().splitlines()
    f.close()

n = len(lines)
X = 1
C = 1
data = np.empty((n + 1, 2))  # X, Y
data[0, :] = [C, X]


def parse_line(line, C, X):
    if "noop" in line:
        C += 1
        # Do nothing
    if "addx" in line:
        operation = int(line.split(" ")[1])
        C += 2
        X += operation

    return C, X, np.array([C, X])


for i, line in enumerate(lines):
    C, X, data[i + 1] = parse_line(line, C, X)

target = [20, 60, 100, 140, 180, 220]

np.sum([data[np.argmin(abs(data[:, 0] - i)), 1] * i for i in target])

## Part 2
df = pd.DataFrame({"x": data[:, 1]}, index=data[:, 0].astype(int))
df = df.reindex(np.arange(1, 241, dtype=int)).ffill()
out = np.empty((6, 40), dtype=str)

for i, (r, c) in enumerate(product(range(0, 6), range(0, 40))):
    x = df.loc[i + 1, "x"]
    sprite = (x - 1, x, x + 1)
    print(i, r, c, x, sprite)
    if c in sprite:
        out[r, c] = "#"
    else:
        out[r, c] = " "

# Render the outputs
for i in range(6):
    print("".join(out[i, :]))
# Bit hard to read
# RGZEHURK
