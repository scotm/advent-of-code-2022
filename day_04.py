def create_set_from_range(r1, r2):
    return set(range(r1, r2 + 1))


puzzle_1_count = 0
puzzle_2_count = 0
with open('day_04_input.txt') as myFile:
    for line in myFile.readlines():
        piece_1, piece_2 = [[int(y) for y in x.split('-')] for x in line.strip().split(',')]
        set_1, set_2 = create_set_from_range(*piece_1), create_set_from_range(*piece_2)
        intersection = set_1.intersection(set_2)

        # If one set overlaps another
        if len(intersection) == len(set_2) or len(intersection) == len(set_1):
            puzzle_1_count += 1

        # If there are any overlaps at all
        if len(intersection) > 0:
            puzzle_2_count += 1

print(f"Answer 1: {puzzle_1_count}")
print(f"Answer 2: {puzzle_2_count}")
