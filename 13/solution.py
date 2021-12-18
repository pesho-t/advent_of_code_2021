#!/usr/bin/env python3

from copy import deepcopy
from typing import List, NamedTuple


class Fold(NamedTuple):
    axis: str
    coord: int


def parse_folds(lines: List[str]) -> List[Fold]:
    folds: List[Fold] = list()

    for line in lines:
        split = line.lstrip("fold along ").split("=")
        folds.append(Fold(axis=split[0], coord=int(split[1])))

    return folds


def fold_grid(grid: List[List[int]], axis: str, coord: int) -> List[List[int]]:
    folded: List[List[int]] = list()
    grid_copy = deepcopy(grid)

    if axis == "x":
        dest_start = 0
        src_start = len(grid_copy) - 1
        while dest_start < coord < src_start:
            for y in range(len(grid_copy[0])):
                grid_copy[dest_start][y] = 1 if grid_copy[dest_start][y] or grid_copy[src_start][y] else 0
            dest_start += 1
            src_start -= 1

        for x in range(coord):
            folded.append(grid_copy[x])

        return folded
    elif axis == "y":
        dest_start = 0
        src_start = len(grid_copy[0]) - 1
        while dest_start < coord < src_start:
            for x in range(len(grid_copy)):
                grid_copy[x][dest_start] = 1 if grid_copy[x][dest_start] or grid_copy[x][src_start] else 0
            dest_start += 1
            src_start -= 1

        for col in grid_copy:
            folded.append(col[:coord])

        return folded
    else:
        ValueError("Wrong folding axes")


def print_grid(grid: List[List[int]]) -> None:
    for y in range(len(grid[0])):
        row = ""
        for x in range(len(grid)):
            row += "#" if grid[x][y] else " "
        print(row)


def main():
    with open("input13") as f:
        lines = f.readlines()

        coords: List[str] = list()

        while True:
            coord = lines.pop(0)
            if coord == "\n":
                break
            coords.append(coord)

        folds = parse_folds(lines)

        max_x = 0
        max_y = 0
        for fold in folds:
            if fold.axis == "x":
                max_x = max(max_x, fold.coord * 2 + 1)
            elif fold.axis == "y":
                max_y = max(max_y, fold.coord * 2 + 1)
            else:
                ValueError(f"Invalid axis: {fold.axis}")

        grid = [[0 for _ in range(max_y)] for _ in range(max_x)]

        for coord in coords:
            x, y = coord.rstrip("\n").split(",")
            grid[int(x)][int(y)] = 1

        # Part 1
        fold = folds.pop(0)
        folded = fold_grid(grid, fold.axis, fold.coord)

        grid_sum = 0
        for col in folded:
            for cell in col:
                grid_sum += cell

        print(f"P1: {grid_sum}")

        # Part 2
        for fold in folds:
            folded = fold_grid(folded, fold.axis, fold.coord)

        print_grid(folded)


if __name__ == "__main__":
    main()
