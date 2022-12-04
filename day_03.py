from typing import List

translation_table = {chr(s + ord('a') - 1): s for s in range(1, 27)}
translation_table.update({chr(s + ord('A') - 1): s + 26 for s in range(1, 27)})


def chunk(this_list: List, chunk_size):
    for i in range(0, len(this_list), chunk_size):
        yield this_list[i:i + chunk_size]


priority_sum = 0
group_priority_sum = 0

with open('day_03_input.txt') as myFile:
    for line in myFile.readlines():
        line = line.strip()
        piece_1, piece_2 = line[:int(len(line) / 2)], line[int(len(line) / 2):]
        piece_1, piece_2 = set(piece_1), set(piece_2)
        common_set = piece_1.intersection(piece_2)
        priority_sum += translation_table[list(common_set)[0]]

    # Taking Problem 2
    myFile.seek(0)
    groups = myFile.readlines()
    for group in chunk(groups, 3):
        group = [x.strip() for x in group]
        this_set = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        group_priority_sum += translation_table[list(this_set)[0]]

print("Answer 1: "+str(priority_sum))
print("Answer 2: "+str(group_priority_sum))
