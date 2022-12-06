def window_gen(this_list, window_size):
    buffer = []
    for i in range(0, len(this_list)):
        if len(buffer) == window_size:
            buffer.pop(0)
        buffer.append(this_list[i])
        if len(buffer) == window_size:
            yield buffer


with open('day_06_input.txt') as myFile:
    data = myFile.read().strip()


def find_valid_marker(input_stream, window_size=4):
    input_length = window_size - 1
    for window in window_gen(input_stream, window_size):
        input_length += 1
        if len(set(window)) == len(window):
            break
    return input_length


# Given test data
tests = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19), ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
         ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23), ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
         ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)]

for test, expected_1, expected_2 in tests:
    if find_valid_marker(test) != expected_1:
        raise Exception
    if find_valid_marker(test, 14) != expected_2:
        raise Exception

print(f'Answer 1: {find_valid_marker(data)}')
print(f'Answer 2: {find_valid_marker(data, 14)}')
