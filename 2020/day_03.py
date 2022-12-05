from functools import reduce

with open('day_03_input.txt') as myFile:
    data = myFile.read().strip().split("\n")

# Instruction list
# ---------------
# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

instructions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
results = []
for instruction in instructions:
    right, down, count_trees = 0, 0, 0
    if data[down][right] == '#':
        count_trees += 1
    while down < len(data) - 1:
        down += instruction[1]
        right = (right + instruction[0]) % len(data[0])
        if data[down][right] == '#':
            count_trees += 1
    results.append(count_trees)

print(f'Answer 1: {results[1]}')
print(f'Answer 2: {reduce(lambda x, y: x * y, results)}')
