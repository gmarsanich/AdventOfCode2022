def main():
    matches = []
    with open("input.txt") as f:
        for line in f:
            match = tuple(line.split())
            matches.append(match)

    scores = {"A": 1, "B": 2, "C": 3}
    move_map = {"X": "A", "Y": "B", "Z": "C"}  # A: rock, B: paper, C: scissors

    total_score = 0
    for match in matches:
        opp_move = match[0]
        my_move = move_map[match[1]]
        total_score += scores[my_move]
        if opp_move == my_move:
            total_score += 3
        elif opp_move == "A" and my_move == "B":
            total_score += 6
        elif opp_move == "B" and my_move == "C":
            total_score += 6
        elif opp_move == "C" and my_move == "A":
            total_score += 6
    print(total_score)


if __name__ == "__main__":
    main()
