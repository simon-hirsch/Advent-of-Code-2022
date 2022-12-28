import numpy as np
import pandas as pd
import string

file = "day_03_input.txt"

with open(file, "r") as f:
    lines = f.read().splitlines()
    f.close()

## Split in 2 equally sized compartments
split = [int(len(i) / 2) for i in lines]
compartment_1 = [i[:k] for i, k in zip(lines, split)]
compartment_2 = [i[k:] for i, k in zip(lines, split)]

rucksack = pd.DataFrame(
    {"compartment_1": compartment_1, "compartment_2": compartment_2}
)

rucksack.loc[:, "intersection"] = rucksack.apply(
    lambda x: "".join(set(x.compartment_1).intersection(x.compartment_2)), axis=1
)

points_lower = {a: p for a, p in zip(string.ascii_lowercase, range(1, 27))}
points_upper = {a: p for a, p in zip(string.ascii_uppercase, range(27, 53))}
points = points_lower | points_upper
points

rucksack.loc[:, "points"] = rucksack.intersection.replace(points)
rucksack.loc[:, "points"].sum()

## Part 2
selector = np.arange(0, len(lines) + 1, step=3, dtype=int)
output = pd.DataFrame(0, columns=["badge"], index=range(0, 100))

for k, (i, j) in enumerate(zip(selector, selector[1:])):
    rucksacks = lines[i:j]
    badge = set(rucksacks[0]).intersection(rucksacks[1]).intersection(rucksacks[2])
    output.loc[k, "badge"] = "".join(badge)

output.loc[:, "priority"] = output.badge.replace(points)
output.loc[:, "priority"].sum()
