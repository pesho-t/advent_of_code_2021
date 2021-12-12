#!/usr/bin/env python3

from typing import List, Tuple


class Grid:
    def __init__(self, lines: List[str]):
        self.height = 10
        self.width = 10
        self.grid = [[0 for _ in range(self.height)] for _ in range(self.width)]

        for y in range(self.height):
            stripped = lines[y].rstrip()

            for x in range(self.width):
                self.grid[x][y] = int(stripped[x])

    def tick(self) -> int:
        to_increment: List[Tuple[int, int]] = list()

        flashes: int = 0

        for y in range(self.height):
            for x in range(self.width):
                self.grid[x][y] += 1
                if self.grid[x][y] == 10:
                    if x > 0:
                        to_increment.append((x-1, y))
                        if y > 0:
                            to_increment.append((x - 1, y - 1))
                        if y < self.height - 1:
                            to_increment.append((x - 1, y + 1))
                    if x < self.width - 1:
                        to_increment.append((x+1, y))
                        if y > 0:
                            to_increment.append((x + 1, y - 1))
                        if y < self.height - 1:
                            to_increment.append((x + 1, y + 1))
                    if y > 0:
                        to_increment.append((x, y-1))
                    if y < self.height - 1:
                        to_increment.append((x, y+1))

        i = 0
        while i < len(to_increment):
            x, y = to_increment[i]

            if self.grid[x][y] < 9:
                self.grid[x][y] += 1
                i += 1
                continue

            if self.grid[x][y] == 9:
                self.grid[x][y] += 1
                if x > 0:
                    to_increment.append((x-1, y))
                    if y > 0:
                        to_increment.append((x - 1, y - 1))
                    if y < self.height - 1:
                        to_increment.append((x - 1, y + 1))
                if x < self.width - 1:
                    to_increment.append((x+1, y))
                    if y > 0:
                        to_increment.append((x + 1, y - 1))
                    if y < self.height - 1:
                        to_increment.append((x + 1, y + 1))
                if y > 0:
                    to_increment.append((x, y-1))
                if y < self.height - 1:
                    to_increment.append((x, y+1))

            i += 1

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[x][y] > 9:
                    flashes += 1
                    self.grid[x][y] = 0

        return flashes

    def print(self):
        header = "  |"
        divider = "--+"
        for x in range(self.width):
            header += f"{x:3}"
            divider += "---"
        print(header)
        print(divider)
        for y in range(self.height):
            row = f"{y} |"
            for x in range(self.width):
                row += f"{self.grid[x][y]:3}"
            print(row)


def part_one(lines: List[str]) -> int:
    grid = Grid(lines)

    flashes = 0

    for i in range(100):
        flashes += grid.tick()

    return flashes


def part_two(lines: List[str]) -> int:
    grid = Grid(lines)

    ticks = 0
    while True:
        flashes = grid.tick()
        ticks += 1

        if flashes == 100:
            return ticks


def main():
    # grid = Grid(["392", "101", "293"])
    # flashes = 0
    # for i in range(100):
    #     flashes += grid.tick()
    #
    # return

    with open("input11") as f:
        lines = f.readlines()

        print(f"P1: {part_one(lines)}")
        print(f"P2: {part_two(lines)}")


if __name__ == "__main__":
    main()
