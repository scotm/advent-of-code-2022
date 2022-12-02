themTable = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
usTable = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

outcomeTable = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
outcomeDecision = {'Rock': {'Win': 'Paper', 'Lose': 'Scissors', 'Draw': 'Rock'},
                   'Paper': {'Win': 'Scissors', 'Lose': 'Rock', 'Draw': 'Paper'},
                   'Scissors': {'Win': 'Rock', 'Lose': 'Paper', 'Draw': 'Scissors'}}


def calculate_base_score(us):
    if us == 'Rock':
        return 1
    elif us == 'Paper':
        return 2
    elif us == 'Scissors':
        return 3
    raise Exception('cant get here')


def calculate_main_score(us, them):
    if us == them:
        return 3
    if (us == 'Rock' and them == 'Scissors') or (us == 'Paper' and them == 'Rock') or (
            us == 'Scissors' and them == 'Paper'):
        return 6
    return 0


def __main__():
    puzzle_1_total = 0
    puzzle_2_total = 0
    with open('day_02_input.txt') as myFile:
        for x in myFile.readlines():
            them, us = x.strip().split(" ")
            puzzle_2_outcome = outcomeTable[us]
            them, us = themTable[them], usTable[us]
            base_score = calculate_base_score(us)
            score = calculate_main_score(us, them)
            puzzle_1_total += base_score + score

            us = outcomeDecision[them][puzzle_2_outcome]
            base_score = calculate_base_score(us)
            score = calculate_main_score(us, them)
            puzzle_2_total += base_score + score

    print("Solution for puzzle 1: " + str(puzzle_1_total))
    print("Solution for puzzle 2: " + str(puzzle_2_total))


__main__()
