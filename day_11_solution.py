import numpy as np

file = "day_11_input_test.txt"
file = "day_11_input.txt"

with open(file, "r") as f:
    lines = f.read().splitlines()
    f.close()

sep = [0] + [i for i in range(len(lines)) if lines[i] == ""] + [len(lines) + 1]


class Monkey:
    def __init__(self, lines) -> None:

        if lines[0] == "":
            lines = lines[1:]

        self.number = int(lines[0].split(" ")[1].replace(":", ""))
        self.items = [*map(int, lines[1].split(":")[1].split(","))]
        self.operation = "add" if "+" in lines[2] else "multiply"
        if self.operation == "add":
            self.operation_value = int(lines[2].split("+")[1])
        else:
            operation_value = lines[2].split("*")[1]
            if "old" in operation_value:
                self.operation = "square"
            else:
                self.operation_value = int(operation_value)
        self.test_value = int(lines[3].split("divisible by")[1])
        self.test_true = int(lines[4].split("monkey")[1])
        self.test_false = int(lines[5].split("monkey")[1])
        self.item_counter = 0

    def inspect_item(self, worry_level):
        self.item_counter += 1
        if self.operation == "add":
            return worry_level + self.operation_value
        if self.operation == "multiply":
            return worry_level * self.operation_value
        if self.operation == "square":
            return worry_level**2

    def get_bored(self, worry_level):
        return int(np.floor(worry_level / 3))

    def do_test(self, worry_level):
        if worry_level % self.test_value == 0:
            return self.test_true
        else:
            return self.test_false

    def handle_item(self, item, part_1=False):
        worry_level = self.inspect_item(item)
        worry_level = self.get_bored(worry_level)
        other_monkey = self.do_test(worry_level)
        self.items.remove(item)
        return other_monkey, worry_level

    def play_round(self):
        t = []
        for item in self.items.copy():
            out = self.handle_item(item)
            t.append(out)
        return t

    def get_new_items(self, new_items):
        for item in new_items:
            if item[0] == self.number:
                self.items.append(item[1])


rounds = 20
monkeys = []
for i, j in zip(sep, sep[1:]):
    monkeys.append(Monkey(lines[i:j]))

for r in range(rounds):
    for monkey in monkeys:
        throws = monkey.play_round()
        for m in monkeys:
            m.get_new_items(throws)

items = [m.items for m in monkeys]
count = np.array([m.item_counter for m in monkeys])

print("Solution Part 1:", np.cumprod(count[np.argpartition(count, -2)[-2:]])[-1])


### Part 2
## Does not work!!


class Monkey_Part_2:
    def __init__(self, lines) -> None:

        if lines[0] == "":
            lines = lines[1:]

        self.number = int(lines[0].split(" ")[1].replace(":", ""))
        self.items = [*map(int, lines[1].split(":")[1].split(","))]
        self.operation = "add" if "+" in lines[2] else "multiply"
        if self.operation == "add":
            self.operation_value = int(lines[2].split("+")[1])
        else:
            operation_value = lines[2].split("*")[1]
            if "old" in operation_value:
                self.operation = "square"
            else:
                self.operation_value = int(operation_value)
        self.test_value = int(lines[3].split("divisible by")[1])
        self.test_true = int(lines[4].split("monkey")[1])
        self.test_false = int(lines[5].split("monkey")[1])
        self.item_counter = 0

    def inspect_item(self, worry_level):
        self.item_counter += 1
        if self.operation == "add":
            return worry_level + self.operation_value
        if self.operation == "multiply":
            return worry_level * self.operation_value
        if self.operation == "square":
            return worry_level**2

    def do_test(self, worry_level):
        if worry_level % self.test_value == 0:
            return self.test_true
        else:
            return self.test_false

    def handle_item(self, item, common):
        worry_level = self.inspect_item(item)
        ## Appearantly we can do this
        ## But it does not give the desired result
        worry_level = worry_level % common
        other_monkey = self.do_test(worry_level)
        self.items.remove(item)
        return other_monkey, worry_level

    def play_round(self, common):
        t = []
        for item in self.items.copy():
            out = self.handle_item(item, common)
            t.append(out)
        return t

    def get_new_items(self, new_items):
        for item in new_items:
            if item[0] == self.number:
                self.items.append(item[1])


rounds = 10000
monkeys = []
for i, j in zip(sep, sep[1:]):
    monkeys.append(Monkey_Part_2(lines[i:j]))

common = 1
for m in monkeys:
    common *= m.test_value

for r in range(rounds):
    for monkey in monkeys:
        throws = monkey.play_round(common)
        for m in monkeys:
            m.get_new_items(throws)

count = np.array([m.item_counter for m in monkeys])
highest = count[np.argpartition(count, -2)[-2:]]

print("Solution Part 2:", int(highest[0]) * int(highest[1]))
