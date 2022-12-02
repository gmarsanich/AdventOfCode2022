def main():
    matches = []
    with open("input.txt") as f:
        for line in f:
            match = tuple(line.split())
            matches.append(match)

    total_score = 0

    for match in matches:
        opp_move = match[0]
        outcome = match[1]

        if opp_move == "A":
            if outcome == "Y":
                total_score += 3 + 1
            elif outcome == "Z":
                total_score += 6 + 2
            else:
                total_score += 3

        elif opp_move == "B":
            if outcome == "Y":
                total_score += 3 + 2
            elif outcome == "Z":
                total_score += 6 + 3
            else:
                total_score += 1

        else:
            if outcome == "Y":
                total_score += 3 + 3
            elif outcome == "Z":
                total_score += 6 + 1
            else:
                total_score += 2
    print(total_score)


if __name__ == "__main__":
    main()
