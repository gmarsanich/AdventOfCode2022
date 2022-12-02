with open("calories.txt", "r") as fp:
    f = fp.read()
    lst = f.split("\n\n")
    calories = [line.split("\n") for line in lst]

sumlist = [sum([int(n) for n in sub if n != ""]) for sub in calories]


part1 = max(sumlist)
print(f"Part 1: {part1}")

part2 = sum(sorted(sumlist)[-3:])
print(f"Part 2: {part2}")
