horizontal_position, depth = 0, 0

with open('day_02_input.txt') as myFile:
    data = [x.strip().split() for x in myFile.readlines()]

for line in data:
    direction, amount = line
    amount = int(amount)
    if direction == 'forward':
        horizontal_position += amount
    elif direction == 'down':
        depth += amount
    elif direction == 'up':
        depth -= amount
    # else:
    #     print(direction)
    #     raise Exception

new_horizontal_position, new_depth, aim = 0, 0, 0
for line in data:
    direction, amount = line
    amount = int(amount)
    if direction == 'forward':
        new_horizontal_position += amount
        new_depth += aim * amount
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount
    pass

print(f'Answer 1: The product of horizontal position and depth is - {horizontal_position * depth}')
print(f'Answer 2: The product of horizontal position and depth is - {new_horizontal_position * new_depth}')