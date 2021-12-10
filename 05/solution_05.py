#!/usr/bin/env python3

from typing import List


def is_suitable(x1: int, y1: int, x2: int, y2: int) -> bool:
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True

    return False


def parse_line(line: str) -> (int, int, int, int):
    tokens = line.rstrip("\n").split(" -> ")
    l_tokens = tokens[0].split(",")
    r_tokens = tokens[1].split(",")
    return int(l_tokens[0]), int(l_tokens[1]), int(r_tokens[0]), int(r_tokens[1])


class Grid:
    def __init__(self):
        self.num_rows = 1
        self.num_cols = 1
        self.grid: List[List[int]] = [[0]]

    def add_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if not is_suitable(x1, y1, x2, y2):
            return

        rows_needed = max(y1, y2) + 1
        if self.num_rows < rows_needed:
            for col in self.grid:
                col.extend([0 for _ in range(rows_needed - self.num_rows)])
            self.num_rows = rows_needed

        cols_needed = max(x1, x2) + 1
        if self.num_cols < cols_needed:
            self.grid.extend([[0 for _ in range(self.num_rows)] for _ in range(cols_needed - self.num_cols)])
            self.num_cols = cols_needed

        if x1 == x2:
            self._mark_vertical(x1, y1, y2)
        elif y1 == y2:
            self._mark_horizontal(y1, x1, x2)
        elif abs(x1 - x2) == abs(y1 - y2):
            self._mark_diagonal(x1, y1, x2, y2)

    def _mark_horizontal(self, y: int, x1: int, x2: int) -> None:
        start, end = (x1, x2) if x1 < x2 else (x2, x1)
        for x in range(start, end+1):
            self.grid[x][y] += 1

    def _mark_vertical(self, x: int, y1: int, y2: int) -> None:
        start, end = (y1, y2) if y1 < y2 else (y2, y1)
        for y in range(start, end+1):
            self.grid[x][y] += 1

    def _mark_diagonal(self, x1: int, y1: int, x2: int, y2: int) -> None:
        x_direction = 1 if x1 < x2 else -1
        y_direction = 1 if y1 < y2 else -1

        x = x1
        y = y1

        x_end = x2 + x_direction
        y_end = y2 + y_direction

        while x != x_end and y != y_end:
            self.grid[x][y] += 1
            x += x_direction
            y += y_direction

    def print(self) -> None:
        for y in range(self.num_rows):
            row = []
            for col in self.grid:
                row.append(str(col[y]))
            print(" ".join(row))


def main():
    grid = Grid()

    with open("input05") as f:
        for line in f.readlines():
            x1, y1, x2, y2 = parse_line(line.rstrip("\n"))
            grid.add_line(x1, y1, x2, y2)

    count = 0

    for col in grid.grid:
        for cell in col:
            if cell> 1:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
