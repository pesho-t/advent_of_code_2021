#!/usr/bin/env python3

def main():
    with open("input") as aoc_in:
        lines = aoc_in.readlines()
        x = 0
        depth = 0
        aim = 0

        for line in lines:
            tokens = line.split(" ")
            cmd = tokens[0]
            scalar = int(tokens[1])

            if cmd == "forward":
                x += scalar
                depth += (aim * scalar)
            elif cmd == "down":
                aim += scalar
            elif cmd == "up":
                aim -= scalar
            else:
                raise ValueError(f"invalid command {cmd}")

        print(f"x: {x}, depth: {depth}, mul: {x*depth}")


if __name__ == "__main__":
    main()
