def part_one():
    # read input
    data = open('input.txt', 'r').read().split('\n')

    total_score = round_score = 0
    for entry in data:
        elf_shape, player_shape = entry.split(' ')

        # elf shape: A = rock, B = paper, C = scissors
        # player shape: X = rock, Y = paper, Z = scissors
        # player shape score : X = 1, Y = 2, Z = 3
        # round score: lose = 0, draw = 3, win = 6
        if player_shape == 'X':
            # shape score
            round_score += 1

            # match score (draw and win)
            if elf_shape == 'A':
                round_score += 3
            elif elf_shape == 'C':
                round_score += 6

        elif player_shape == 'Y':
            # shape score
            round_score += 2

            # match score (draw and win)
            if elf_shape == 'B':
                round_score += 3
            elif elf_shape == 'A':
                round_score += 6

        elif player_shape == 'Z':
            # shape score
            round_score += 3

            # match score (draw and win)
            if elf_shape == 'C':
                round_score += 3
            elif elf_shape == 'B':
                round_score += 6

        total_score += round_score
        round_score = 0
    print(f'Part One Total Score: {total_score}')


def part_two():
    # read input
    data = open('input.txt', 'r').read().split('\n')

    total_score = round_score = 0
    for entry in data:
        elf_shape, match_result = entry.split(' ')

        if match_result == 'X':
            round_score += 0  # lose
            if elf_shape == 'A':
                round_score += 3  # scissors
            if elf_shape == 'B':
                round_score += 1  # rock
            if elf_shape == 'C':
                round_score += 2  # paper
        elif match_result == 'Y':
            round_score += 3  # draw
            if elf_shape == 'A':
                round_score += 1  # rock
            if elf_shape == 'B':
                round_score += 2  # paper
            if elf_shape == 'C':
                round_score += 3  # scissors
        elif match_result == 'Z':
            round_score += 6  # win
            if elf_shape == 'A':
                round_score += 2  # paper
            if elf_shape == 'B':
                round_score += 3  # scissors
            if elf_shape == 'C':
                round_score += 1  # rock
        total_score += round_score
        round_score = 0
    print(f'Part Two Total Score: {total_score}')


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
