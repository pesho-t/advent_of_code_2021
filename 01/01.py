#!/usr/bin/env python3


def main():
    increments = 0

    w_o = 0
    w_c = 2

    with open("input") as aoc_in:
        lines = aoc_in.readlines()
        sum = int(lines[w_o]) + int(lines[w_o + 1]) + int(lines[w_c])
        while w_c < len(lines):
            if w_o == 0:
                w_o += 1
                w_c += 1
                continue

            old_sum = sum
            sum -= int(lines[w_o - 1])
            sum += int(lines[w_c])

            if sum > old_sum:
                increments += 1
            w_o += 1
            w_c += 1

        print(increments)


if __name__ == "__main__":
    main()
