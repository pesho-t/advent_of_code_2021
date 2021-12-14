#!/usr/bin/env python3

from typing import List, NamedTuple, Tuple

class Fold(NamedTuple):
    axis: str
    coord: int


def parse_coords(coords: List[str]) -> List[List[int]]:
    grid: List[List[int]] = [[0]]
    width = 1
    height = 1

    for pair in coords:
        x_str, y_str = pair.strip("\n").split(",")
        x = int(x_str)
        y = int(y_str)

        if y + 1 > height:
            for col in grid:
                col.extend([0 for _ in range(y + 1 - height)])
            height = y + 1

        if x + 1 > width:
            grid.extend([[0 for _ in range(height)] for _ in range(x + 1 - width)])
            width = x + 1

        grid[x][y] = 1

    return grid


def parse_folds(lines: List[str]) -> List[Fold]:
    folds: List[Fold] = list()

    for line in lines:
        split = line.lstrip("fold along ").split("=")
        folds.append(Fold(axis=split[0], coord=int(split[1])))

    return folds


def slice_grid(grid: List[List[int]], axis: str, coord: int) -> Tuple[List[List[int]], List[List[int]]]:
    if axis == "x":
        top: List[List[int]] = list()
        bottom: List[List[int]] = list()

        for col in grid:
            top.append(col[:coord])
            bottom.append(col[coord+1:])
            return top, bottom
    elif axis == "y":
        left = grid[:coord]
        right = grid[coord+1:]
        return left, right
    else:
        raise ValueError(f"Invalid axis {axis}")


def fold_grid(grid: List[List[int]], axis: str, coord: int) -> List[List[int]]:
    folded: List[List[int]] = list()
    grid_copy = grid.copy()

    if axis == "x":
        dest_start = 0
        src_start = len(grid) - 1
        while dest_start < coord < src_start:
            for y in range(len(grid[0])):
                grid_copy[dest_start][y] = 1 if grid[dest_start][y] or grid[src_start][y] else 0
            dest_start += 1
            src_start -= 1

        for x in range(coord):
            folded.append(grid_copy[x])

        return folded
    else:
        ValueError("Wrong folding axes")


def main():
    with open("input13") as f:
        lines = f.readlines()

        coords: List[str] = list()

        while True:
            coord = lines.pop(0)
            if coord == "\n":
                break
            coords.append(coord)

        grid = parse_coords(coords)

        folds = parse_folds(lines)

        # Part 1
        folded = fold_grid(grid, folds[0].axis, folds[0].coord)
        grid_sum = 0
        for col in folded:
            for cell in col:
                grid_sum += cell

        print(grid_sum)


if __name__ == "__main__":
    main()
