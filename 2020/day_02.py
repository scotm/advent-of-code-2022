with open('day_02_input.txt') as myFile:
    data = myFile.read().strip().split("\n")

puzzle_1_valid = 0
puzzle_2_valid = 0
x: str
for x in data:
    policy: str
    password: str
    policy, password = x.split(":")
    password = password.strip()
    temp1, policy_letter = policy.split(" ")
    temp2 = [int(x) for x in temp1.split("-")]
    policy_range = set(range(temp2[0], temp2[1] + 1))
    if password.count(policy_letter) in policy_range:
        puzzle_1_valid += 1
    # off-by-one check - also, it's an *exclusive or!*
    if (password[temp2[0] - 1] == policy_letter) != (password[temp2[1] - 1] == policy_letter):
        puzzle_2_valid += 1

print(f"Answer 1: {puzzle_1_valid}")
print(f"Answer 2: {puzzle_2_valid}")
