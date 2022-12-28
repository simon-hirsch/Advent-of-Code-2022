import pandas as pd
import numpy as np

file = "day_04_input.txt"

input = pd.read_csv(
    filepath_or_buffer="day_04_input.txt",
    sep=",",
    header=None,
    names=["elf_a", "elf_b"],
)

input[["elf_a_start", "elf_a_stop"]] = pd.DataFrame(
    input.elf_a.str.split("-").to_list()
).astype(int)
input[["elf_b_start", "elf_b_stop"]] = pd.DataFrame(
    input.elf_b.str.split("-").to_list()
).astype(int)
input["b_contains_a"] = input.elf_a_start.ge(input.elf_b_start) & input.elf_a_stop.le(
    input.elf_b_stop
)
input["a_contains_b"] = input.elf_b_start.ge(input.elf_a_start) & input.elf_b_stop.le(
    input.elf_a_stop
)

input.head()
input.tail()

input["fully_contained"] = input.b_contains_a | input.a_contains_b
input.fully_contained.sum()

## Part 2

input["b_overlaps_a"] = (
    input.elf_a_start.ge(input.elf_b_start) & input.elf_a_start.le(input.elf_b_stop)
) | (input.elf_a_stop.ge(input.elf_b_start) & input.elf_a_stop.le(input.elf_b_stop))

input["a_overlaps_b"] = (
    input.elf_b_start.ge(input.elf_a_start) & input.elf_b_start.le(input.elf_a_stop)
) | (input.elf_b_stop.ge(input.elf_a_start) & input.elf_b_stop.le(input.elf_a_stop))

(input.a_overlaps_b | input.b_overlaps_a).sum()
