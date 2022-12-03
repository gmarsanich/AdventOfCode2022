from string import ascii_letters


def main():
    with open("input.txt", "r") as fp:
        rucksacks = fp.readlines()
        rucksacks = [r.strip() for r in rucksacks]

    groups = [rucksacks[r : r + 3] for r in range(0, len(rucksacks), 3)]

    sum_of_priorities = 0

    for group in groups:
        common = list(set.intersection(*[set(ch for ch in i) for i in group]))
        if common[0] in ascii_letters:
            # Priority => index(item) + 1
            sum_of_priorities += ascii_letters.index(common[0]) + 1

    print(sum_of_priorities)


if __name__ == "__main__":
    main()
