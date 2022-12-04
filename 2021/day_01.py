def window(iterable, window_length=1):
    data = []
    i = iter(iterable)
    while True:
        try:
            d = next(i)
        except StopIteration:
            break
        d = int(d.strip())
        data.append(d)
        if len(data) == window_length:
            yield data
            data.pop(0)


puzzle_1_count = 0
puzzle_2_count = 0
with open('day_01_input.txt') as myFile:
    prev_value = None
    for x in window(myFile.readlines()):
        if prev_value is not None and x[0] > prev_value:
            puzzle_1_count += 1
        prev_value = x[0]

with open('day_01_input.txt') as myFile:
    prev_sum = None
    for x in window(myFile.readlines(), 3):
        if prev_sum is not None and sum(x) > prev_sum:
            puzzle_2_count += 1
        prev_sum = sum(x)

print(puzzle_1_count)
print(puzzle_2_count)
