def window_gen(this_list, window_size):
    buffer = list(this_list[:window_size])
    for i in this_list[window_size:]:
        buffer.pop(0)
        buffer.append(i)
        yield buffer


def find_valid_marker(input_stream, window_size):
    marker_position = window_size
    for window in window_gen(input_stream, window_size):
        marker_position += 1
        if len(set(window)) == window_size:
            break
    return marker_position


with open('day_06_input.txt') as myFile:
    data = myFile.read().strip()

# Given test data
tests = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19), ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
         ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23), ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
         ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)]

for test, expected_1, expected_2 in tests:
    if find_valid_marker(test, 4) != expected_1:
        raise Exception
    if find_valid_marker(test, 14) != expected_2:
        raise Exception

print(f'Answer 1: {find_valid_marker(data, 4)}')
print(f'Answer 2: {find_valid_marker(data, 14)}')
