from pprint import pprint

SIZE_KEY = '#thisdirectoryssizeis'

with open('day_07_input.txt') as myFile:
    listing = [x.strip() for x in myFile.read().strip().split("\n")]

# listing = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""".split("\n")

filesystem = {}

current_directory = []


def resolve_current_directory(fs, cd):
    # drill into the filesystem
    temp = fs
    for x in cd:
        temp = temp[x]
    return temp


def find_all_directories(fs):
    for x in fs:
        if isinstance(fs[x], dict):
            yield x, fs[x]
            for y in find_all_directories(fs[x]):
                yield y


lines = iter(listing)
this_line = next(lines).split()
try:
    while True:
        if this_line[0] == '$':
            if this_line[1] == 'cd':
                if this_line[2] == '/':
                    current_directory = []
                elif this_line[2] == '..':
                    current_directory.pop()
                else:
                    current_directory.append(this_line[2])
                this_line = next(lines).split()
                continue
            if this_line[1] == 'ls':
                while True:
                    this_line = next(lines).split()
                    if this_line[0] == '$':
                        break
                    else:
                        this_filesystem = resolve_current_directory(filesystem, current_directory)
                        if this_line[0] == 'dir':
                            # Add a dictionary - representing a directory to the filesystem
                            this_filesystem[this_line[1]] = {}
                        else:
                            this_filesystem[this_line[1]] = int(this_line[0])
except StopIteration:
    pass


def calculate_directory_sizes(directory):
    directory_sum = 0
    if SIZE_KEY in directory:
        return directory[SIZE_KEY]
    for element in directory:
        if isinstance(directory[element], int):
            directory_sum += directory[element]
        elif isinstance(directory[element], dict):
            directory_sum += calculate_directory_sizes(directory[element])
    directory[SIZE_KEY] = directory_sum
    return directory_sum


calculate_directory_sizes(filesystem)

# Solution to question 1
question_1_solution = sum(
    directory[SIZE_KEY] for _, directory in find_all_directories(filesystem) if directory[SIZE_KEY] <= 100000)
print(f'Answer to Problem 1 = {question_1_solution}')

required = 30000000
available = 70000000 - filesystem[SIZE_KEY]
need_free = required - available

# print(f'We need to find a directory containing more than {need_free}')
suitable_directories = min(directory[SIZE_KEY] for _, directory in find_all_directories(filesystem) if
                           directory[SIZE_KEY] >= need_free)
print(f'Answer to Problem 2 = {suitable_directories}')
