file = "day_06_input.txt"

with open(file, "r") as f:
    lines = f.read()
    f.close()

N = len(lines)
# n_distinct_characters = 4
n_distinct_characters = 14

for i, j in zip(range(0, N), range(n_distinct_characters, N)):
    subset = lines[i:j]
    if len(set(subset)) == n_distinct_characters:
        print(j)
        break
