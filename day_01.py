data: list[list[int]] = []
elf_bundle: list[int] = []

with open('day_01_input.txt') as my_file:
    for x in my_file.readlines():
        x = x.strip()
        if not x:
            data.append(elf_bundle)
            elf_bundle = []
        else:
            elf_bundle.append(int(x))

newData = sorted([sum(x) for x in data])
print("Answer 1: " + str(max(newData)))
topThree = newData[-3:]
print("Answer 2: " + str(sum(topThree)))
