def main():
    # read input
    data = open('input.txt', 'r').read().split('\n')

    # find top 3 elfs with most calories
    elf_first_place = elf_second_place = elf_third_place = 0
    elf_current = 0
    for value in data:
        if value != '':
            elf_current += int(value)
        else:
            if elf_current > elf_first_place:
                elf_third_place = elf_second_place
                elf_second_place = elf_first_place
                elf_first_place = elf_current
            elif elf_current > elf_second_place:
                elf_third_place = elf_second_place
                elf_second_place = elf_current
            elif elf_current > elf_third_place:
                elf_third_place = elf_current
            elf_current = 0

    print(f'Elf 1th: {elf_first_place}')
    print(f'Elf 2th: {elf_second_place}')
    print(f'Elf 3th: {elf_third_place}')
    print(f'Total top 3: {elf_first_place + elf_second_place + elf_third_place}')


if __name__ == "__main__":
    main()
