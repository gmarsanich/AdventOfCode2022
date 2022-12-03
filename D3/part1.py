from string import ascii_letters


def main():
    with open("input.txt", "r") as fp:
        rucksacks = fp.readlines()
        rucksacks = [r.strip() for r in rucksacks]

    sum_of_priorities = 0

    for rucksack in rucksacks:
        compartment_1 = rucksack[: len(rucksack) // 2]
        compartment_2 = rucksack[len(rucksack) // 2 :]

        common = tuple(set(compartment_1) & set(compartment_2))

        if common[0] in ascii_letters:
            # Priority => index(item) + 1
            sum_of_priorities += ascii_letters.index(common[0]) + 1

    print(sum_of_priorities)


if __name__ == "__main__":
    main()
