import re
from collections import defaultdict
from math import floor, lcm

with open('day_11_input.txt') as myFile:
    data = myFile.read().strip().split("\n\n")


def parse_monkeys(monkey_data):
    all_monkeys = defaultdict(dict)
    # Parse monkeys
    for monkey_block in monkey_data:
        monkey_info = monkey_block.split('\n')
        m_id = int(re.search(r'Monkey (\d+):', monkey_info[0]).groups()[0])
        monkey_items = re.search(r'Starting items: ([0-9, ]+)', monkey_info[1]).groups()[0]
        all_monkeys[m_id]['items'] = [int(x) for x in monkey_items.split(', ')]
        all_monkeys[m_id]['operation'] = re.search(r'Operation: (.+)', monkey_info[2]).groups()[0]
        all_monkeys[m_id]['divisibleby_test'] = int(re.search(r'Test: divisible by (\d+)', monkey_info[3]).groups()[0])
        all_monkeys[m_id]['if_true'] = int(re.search(r'If true: throw to monkey (\d+)', monkey_info[4]).groups()[0])
        all_monkeys[m_id]['if_false'] = int(re.search(r'If false: throw to monkey (\d+)', monkey_info[5]).groups()[0])
        all_monkeys[m_id]['times_inspected'] = 0
    return all_monkeys


def perform_operation(operation, item):
    operation = operation.split()[2:]
    if operation[0] == 'old':
        operation[0] = item
    operation[2] = item if operation[2] == 'old' else int(operation[2])
    match operation[1]:
        case '*':
            return operation[0] * operation[2]
        case '+':
            return operation[0] + operation[2]


def do_round(all_monkeys, worry_manager=True, common_factor=None):
    for this_monkey in all_monkeys:
        monkey = all_monkeys[this_monkey]
        for item in monkey['items']:
            # Perform operation
            result = perform_operation(monkey['operation'], item)
            if worry_manager:
                # floor(divide by three)
                result = int(floor(result / 3))
            elif common_factor:
                # how do we keep the worry numbers outside BigInt territory?
                result = result % common_factor

            # test and throw
            if result % monkey['divisibleby_test'] == 0:
                all_monkeys[monkey['if_true']]['items'].append(result)
            else:
                all_monkeys[monkey['if_false']]['items'].append(result)
            monkey['times_inspected'] += 1
        monkey['items'] = []


def calculate_monkey_business(all_monkeys):
    monkey_business = sorted([all_monkeys[monkey]['times_inspected'] for monkey in all_monkeys])[-2:]
    return monkey_business[0] * monkey_business[1]


# SOLUTIONS

monkeys = parse_monkeys(data)
least_common_multiple = lcm(*[x['divisibleby_test'] for x in monkeys.values()])
for _ in range(20):
    do_round(monkeys, worry_manager=True, common_factor=least_common_multiple)
print(f'Answer 1: {calculate_monkey_business(monkeys)}')

monkeys = parse_monkeys(data)
for i in range(10000):
    do_round(monkeys, worry_manager=False, common_factor=least_common_multiple)

print(f'Answer 2: {calculate_monkey_business(monkeys)}')
