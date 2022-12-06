def main():
    with open("input.txt", "r") as fp:
        tmp = fp.readlines()
        tmp = [p.strip() for p in tmp]
        pairs = [pair.split(",") for pair in tmp]

    part1_count = 0
    part2_count = 0

    for pair in pairs:
        tmp = [item.split("-") for item in pair]
        elf1 = set(range(int(tmp[0][0]), int(tmp[0][1]) + 1))
        elf2 = set(range(int(tmp[1][0]), int(tmp[1][1]) + 1))
        if elf1 <= elf2 or elf2 <= elf1:
            part1_count += 1
        if len(elf1.intersection(elf2)) != 0:
            part2_count += 1
    print(f"Part 1: {part1_count}\nPart 2: {part2_count}")


if __name__ == "__main__":
    main()
