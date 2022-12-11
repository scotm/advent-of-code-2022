from itertools import product

with open('day_08_input.txt') as myFile:
    data = myFile.read().strip().split("\n")

debug = True

# data = """30373
# 25512
# 65332
# 33549
# 35390""".split("\n")

# Set up the height matrix
treeHeightMatrix = [[int(y) for y in x] for x in data]

# Go round the outside 2x all sides, subtract 4 for the corners
count_visible_trees = len(treeHeightMatrix) * 2 + len(treeHeightMatrix[0]) * 2 - 4

for x, y in product(range(1, len(treeHeightMatrix) - 1), range(1, len(treeHeightMatrix[0]) - 1)):
    this_height = treeHeightMatrix[x][y]
    # check left, right, up and down
    if all(this_height > treeHeightMatrix[test_x][y] for test_x in range(0, x)) or \
            all(this_height > treeHeightMatrix[test_x][y] for test_x in range(x + 1, len(treeHeightMatrix[0]))) or \
            all(this_height > treeHeightMatrix[x][test_y] for test_y in range(0, y)) or \
            all(this_height > treeHeightMatrix[x][test_y] for test_y in range(y + 1, len(treeHeightMatrix))):
        count_visible_trees += 1

print(f'Answer 1: {count_visible_trees}')


def calculate_scenic_score(x, y):
    tree_height = treeHeightMatrix[x][y]
    left = 0
    for test_x in range(x - 1, -1, -1):
        left += 1
        if tree_height <= treeHeightMatrix[test_x][y]:
            break
    right = 0
    for test_x in range(x + 1, len(treeHeightMatrix[0])):
        right += 1
        if tree_height <= treeHeightMatrix[test_x][y]:
            break
    up = 0
    for test_y in range(y - 1, -1, -1):
        up += 1
        if tree_height <= treeHeightMatrix[x][test_y]:
            break
    down = 0
    for test_y in range(y + 1, len(treeHeightMatrix)):
        down += 1
        if tree_height <= treeHeightMatrix[x][test_y]:
            break
    return left * right * up * down


maximal_scenic_score = max(calculate_scenic_score(x, y) for x, y in
                           product(range(len(treeHeightMatrix)), range(len(treeHeightMatrix[0]))))
print(f'Answer 2: {maximal_scenic_score}')
