data = []
clump = []

with open('day_01_input.txt') as my_file:
    for x in my_file.readlines():
        x = x.strip()
        if not x:
            data.append(clump)
            clump = []
        else:
            clump.append(int(x))

newData = sorted([sum(x) for x in data])
print("Answer 1: " + str(max(newData)))
topThree = newData[-3:]
print("Answer 2: " + str(sum(topThree)))
