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
topThree = newData[-3:]

print(f"Answer 1: {max(newData)}")
print(f"Answer 2: {sum(topThree)}")
