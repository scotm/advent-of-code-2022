from collections import defaultdict
from copy import deepcopy
from re import compile
from utils import chunk

with open('day_05_input.txt') as myFile:
    data = myFile.read()

stacks_data, instructions = data.split("\n\n")

# Construct the stacks. Use a simple dictionary -> list
stacks = defaultdict(list)
for x in stacks_data.split("\n")[:-1]:
    for index, container in enumerate(chunk(x, 4), 1):
        container = container.strip()

        # Many of these chunks are blank - so skip.
        if container:
            # Container has format "[$LETTER]" - so container[1] has the letter we want
            # Insert at base, so we don't have to reverse later
            # (If there were millions of these things, I'd do it differently.)
            stacks[index].insert(0, container[1])

# Duplicate it, because we're going to be changing the original.
duplicate_stacks = deepcopy(stacks)

# regex to capture the instructions
prog = compile(r'move (\d+) from (\d) to (\d)')

for instruction in instructions.strip().split("\n"):
    # Parse each instruction
    number_to_move, column_from, column_to = [int(x) for x in prog.search(instruction).groups()]

    # ANSWER 1
    # Simple enough, pop and push singly
    for iteration in range(number_to_move):
        stacks[column_to].append(stacks[column_from].pop())

    # ANSWER 2
    # Take from the end of each stack as a group
    captured = duplicate_stacks[column_from][-number_to_move:]

    # Remove from the originating column
    for iteration in range(number_to_move):
        duplicate_stacks[column_from].pop()

    # Append to the destination column
    for captured_item in captured:
        duplicate_stacks[column_to].append(captured_item)

# Get the sorted keys and find the last one on top
print("Answer 1: " + "".join(stacks[i][-1] for i in sorted(stacks)))
print("Answer 2: " + "".join(duplicate_stacks[i][-1] for i in sorted(duplicate_stacks)))
