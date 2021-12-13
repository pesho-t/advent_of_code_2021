#!/usr/bin/env python3


def calculate_bits(lines):
    array = [[0, 0] for _ in lines[0].strip("\n")]

    for line in lines:
        for i in range(len(line) - 1):
            array[i][int(line[i])] += 1

    return array


def main():

    with open("input") as aoc_in:
        lines = aoc_in.readlines()

        array = calculate_bits(lines)

        print(array)

        gamma = ["0" if bit[0] > bit[1] else "1" for bit in array]
        print(f"gamma: {gamma}")  # 1174
        epsilon = ["0" if bit[0] < bit[1] else "1" for bit in array]
        print(f"epsilon: {epsilon}")  # 2921

        lines_copy = lines.copy()
        #import pdb; pdb.set_trace()
        for i in range(len(array)):
            array_copy = calculate_bits(lines_copy)
            for line in lines_copy.copy():
                if int(line[i]) != (0 if array_copy[i][0] > array_copy[i][1] else 1):
                    lines_copy.remove(line)

        print(lines_copy)

        lines_copy2 = lines.copy()
        #import pdb; pdb.set_trace()
        for i in range(len(array)):
            array_copy = calculate_bits(lines_copy2)
            for line in lines_copy2.copy():
                if int(line[i]) != (0 if array_copy[i][0] <= array_copy[i][1] else 1):
                    lines_copy2.remove(line)
                if len(lines_copy2) == 1:
                    break
            if len(lines_copy2) == 1:
                print(f"bailing early at idx {i}")
                break

        print(lines_copy2)


if __name__ == "__main__":
    main()
