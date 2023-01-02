import pandas as pd
import numpy as np
from itertools import product

file = "day_08_input.txt"

map = pd.read_fwf(file, widths=np.repeat(1, 99), names=np.arange(0, 99))
n = map.shape[0]
m = map.shape[1]

is_visible = np.zeros((n, m, 4)).astype(bool)
is_visible.shape

## Left to right
for i in np.arange(1, n, step=1, dtype=int):
    is_visible[:, i, 0] = map.loc[:, i].gt(map.loc[:, 0 : (i - 1)].max(axis=1))

## Right to left
for i in np.arange(n - 1, 0, step=-1, dtype=int):
    is_visible[:, i, 1] = map.loc[:, i].gt(map.loc[:, (i + 1) :].max(axis=1))

## Top to bottom
for i in np.arange(1, m, step=1, dtype=int):
    is_visible[i, :, 2] = map.loc[i, :].gt(map.loc[: (i - 1), :].max(axis=0))

## Bottom to top
for i in np.arange(m - 1, 0, step=-1, dtype=int):
    is_visible[i, :, 3] = map.loc[i, :].gt(map.loc[(i + 1) :, :].max(axis=0))

inside = np.any(is_visible, axis=2)
inside[0, :] = True
inside[:, 0] = True
inside[-1, :] = True
inside[:, -1] = True
np.sum(inside)

## Part 2 - Scenic score

view_score = np.zeros((n, m))

for a, b in product(range(n), range(m)):

    tree = (a, b)
    height = map.loc[tree]
    view = np.zeros(4)

    # South
    for i in np.arange(tree[1] + 1, 99, step=1, dtype=int):
        if map.loc[tree[0], i] < height:
            view[0] += 1
        elif map.loc[tree[0], i] == height:
            view[0] += 1
            break
        else:
            break

    # North
    for i in np.arange(tree[1] - 1, -1, step=-1, dtype=int):
        if map.loc[tree[0], i] < height:
            view[1] += 1
        elif map.loc[tree[0], i] == height:
            view[1] += 1
            break
        else:
            break

    # West
    for i in np.arange(tree[0] + 1, 99, step=1, dtype=int):
        if map.loc[i, tree[1]] < height:
            view[2] += 1
        elif map.loc[i, tree[1]] == height:
            view[2] += 1
            break
        else:
            break

    # East
    for i in np.arange(tree[0] - 1, -1, step=-1, dtype=int):
        if map.loc[i, tree[1]] < height:
            view[3] += 1
        elif map.loc[i, tree[1]] == height:
            view[3] += 1
            break
        else:
            break

    view_score[a, b] = np.cumprod(view)[-1]

np.max(view_score)
# Wrong: 500850
# Wrong: 5760000
