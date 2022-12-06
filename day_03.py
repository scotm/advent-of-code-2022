from utils import chunk

translation_table = {chr(s + ord('a') - 1): s for s in range(1, 27)}
translation_table.update({chr(s + ord('A') - 1): s + 26 for s in range(1, 27)})

priority_sum = 0
group_priority_sum = 0

with open('day_03_input.txt') as myFile:
    for line in myFile.readlines():
        line = line.strip()
        piece_1, piece_2 = line[:int(len(line) / 2)], line[int(len(line) / 2):]
        common_set = set(piece_1) & set(piece_2)
        priority_sum += translation_table[list(common_set)[0]]

    # Taking Problem 2 - reset file pointer
    myFile.seek(0)
    for group in chunk(myFile.readlines(), 3):
        group = [x.strip() for x in group]
        this_set = set(group[0]) & set(group[1]) & set(group[2])
        group_priority_sum += translation_table[list(this_set)[0]]

print(f"Answer 1: {priority_sum}")
print(f"Answer 2: {group_priority_sum}")
