from itertools import combinations

with open('day_01_input.txt') as myFile:
    data = myFile.read().strip().split("\n")
data = [int(x) for x in data]
filtered_combinations = [(x, y) for x, y in combinations(data, 2) if x + y == 2020]
more_filtered_combinations = [(x, y, z) for x, y, z in combinations(data, 3) if x + y + z == 2020]
print(filtered_combinations[0][0] * filtered_combinations[0][1])
print(more_filtered_combinations[0][0] * more_filtered_combinations[0][1] * more_filtered_combinations[0][2])
