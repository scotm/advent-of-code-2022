from collections import defaultdict
from copy import deepcopy
from re import compile


def chunk(this_list, chunk_size):
    for i in range(0, len(this_list), chunk_size):
        yield this_list[i:i + chunk_size]


stacks = defaultdict(list)
with open('day_05_input.txt') as myFile:
    data = myFile.read()

stacks_data, instructions = data.split("\n\n")
for x in stacks_data.split("\n")[:-1]:
    for index, y in enumerate(chunk(x, 4), 1):
        y = y.strip()
        if y:
            stacks[index].insert(0, y[1])

duplicate_stacks = deepcopy(stacks)

# regex to capture the instructions
prog = compile("move (\d+) from (\d) to (\d)")

for instruction in instructions.strip().split("\n"):
    number_to_move, column_from, column_to = [int(x) for x in prog.search(instruction).groups()]
    # ANSWER 1
    # Simple enough, pop and push
    for iteration in range(number_to_move):
        stacks[column_to].append(stacks[column_from].pop())

    # ANSWER 2
    # Now we try and solve the second one - take from the end of each stack
    captured = duplicate_stacks[column_from][-number_to_move:]

    # Delete from the originating column
    for iteration in range(number_to_move):
        duplicate_stacks[column_from].pop()

    # Push onto the destination column
    for captured_item in captured:
        duplicate_stacks[column_to].append(captured_item)

print("Answer 1: "+"".join(stacks[i][-1] for i in sorted(stacks)))
print("Answer 2: "+"".join(duplicate_stacks[i][-1] for i in sorted(duplicate_stacks)))
