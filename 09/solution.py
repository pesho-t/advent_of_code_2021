#!/usr/bin/env python3

from typing import List


def main():
    with open("input09") as f:
        lines = f.readlines()

        grid_height = len(lines)
        grid_width = len(lines[0].rstrip("\n"))

        grid: List[List[int]] = [[] for _ in range(grid_width)]
        marks = [["." for _ in range(grid_height)] for _ in range(grid_width)]

        for line in lines:
            line_stripped = line.rstrip("\n")
            for x in range(grid_width):
                grid[x].append(int(line_stripped[x]))

        risk = 0

        for y in range(grid_height):
            x = 0
            while x < grid_width:
                while x < (grid_width - 1) and grid[x][y] >= grid[x+1][y]:
                    x += 1

                compare_to = {grid[x][y]}
                if x > 0:
                    compare_to.add(grid[x-1][y])
                if x < grid_width - 1:
                    compare_to.add(grid[x+1][y])
                if y > 0:
                    compare_to.add(grid[x][y-1])
                if y < grid_height - 1:
                    compare_to.add(grid[x][y+1])

                if len(compare_to) > 1 and sorted(compare_to)[0] == grid[x][y]:
                    marks[x][y] = "o"
                    risk += (1 + grid[x][y])
                x += 1


        print(risk)
        print("\n\n")
        for y in range(grid_height):
            row = ""
            for x in range(grid_width):
                row += marks[x][y]
            #print(row)
        return


        # Four corners
        # 0, 0
        if grid[0] < grid[1] and grid[0] < grid[grid_width]:
            risk += 1 + grid[0]
        # 0, height
        if (
            grid[grid_width * grid_height] < grid[grid_width * (grid_height - 1)]
            and grid[grid_width * grid_height] < grid[grid_width * grid_height + 1]
        ):
            risk += 1 + grid[grid_width * grid_height]
        # Width, 0
        if grid[grid_width - 1] < grid[grid_width - 2] and grid[grid_width - 1] < grid[2 * grid_width - 1]:
            risk += 1 + grid[grid_width - 1]
        # Width, height
        if (
            grid[grid_width * grid_height - 1] < grid[grid_width * grid_height - 2]
            and grid[grid_width * grid_height - 1] < grid[(grid_width - 1) * (grid_height - 1)]
        ):
            risk += 1 + grid[grid_width * grid_height - 1]

        # First row, minus corners
        for x in range(1, grid_width - 2):
            if grid[x] < grid[x-1] and grid[x] < grid[x+1]:
                pass


if __name__ == "__main__":
    main()
