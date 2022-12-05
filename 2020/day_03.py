with open('day_03_input.txt') as myFile:
    data = myFile.read().strip().split("\n")

# data = """..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#""".strip().split("\n")

right, down = 0, 0

count_trees = 0
if data[down][right] == '#':
    count_trees += 1
while down < len(data) - 1:
    down += 1
    right = (right + 3) % len(data[0])
    if data[down][right] == '#':
        count_trees += 1
print(count_trees)
