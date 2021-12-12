#!/usr/bin/env python3

from collections import deque
from typing import Deque


valid_combos = {
    "(": ")",
    "<": ">",
    "{": "}",
    "[": "]"
}

scores_p1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

scores_p2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def process_line_part_one(line: str) -> int:
    expected_closings: Deque[str] = deque()

    for char in line:
        if char in valid_combos.keys():
            expected_closings.append(valid_combos[char])
        else:
            expected = expected_closings.pop()
            if char != expected:
                return scores_p1[char]

    return 0


def process_line_part_two(line: str) -> Deque[str]:
    expected_closings: Deque[str] = deque()

    for char in line:
        if char in valid_combos.keys():
            expected_closings.append(valid_combos[char])
        else:
            expected = expected_closings.pop()
            if char != expected:
                return deque()

    return expected_closings


def main():
    assert process_line_part_one("[") == 0
    assert process_line_part_one("[]") == 0
    assert process_line_part_one("[>") == scores_p1[">"]

    assert process_line_part_two("[") == deque("]")
    assert process_line_part_two("[]") == deque()
    assert process_line_part_two("[>") == deque()
    assert process_line_part_two("[{") == deque(["]", "}"])

    with open("input10") as f:
        lines = f.readlines()

        p1_score = 0

        for line in lines:
            stripped = line.rstrip("\n")
            p1_score += process_line_part_one(stripped)

        print(f"P1: {p1_score}")

        p2_scores = list()

        for line in lines:
            stripped = line.rstrip("\n")
            autocomplete = process_line_part_two(stripped)
            if len(autocomplete) == 0:
                continue

            score = 0
            while True:
                if len(autocomplete) == 0:
                    break

                next_char = autocomplete.pop()
                score *= 5
                score += scores_p2[next_char]
            p2_scores.append(score)

        p2_scores.sort()
        winning_index = int((len(p2_scores) - 1) / 2)
        print(f"P2: {p2_scores[winning_index]}")


if __name__ == "__main__":
    main()
