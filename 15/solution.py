import sys
import heapq
from typing import List, Optional
from dataclasses import dataclass, field


class Node:
    def __init__(self, x: int, y: int, risk: int):
        self.x = x
        self.y = y
        self.risk = risk
        self.children: List[Node] = []
        self.h_val: int = -1
        self.g_val: int = sys.maxsize
        self.visited_from: Optional[Node] = None

    def add_child(self, node):
        self.children.append(node)

    def f_val(self) -> int:
        return self.g_val + self.h_val

    def __repr__(self):
        return f"x: {self.x}, y: {self.y} ({self.risk})"

    def __hash__(self):
        return hash(f"{self.x},{self.y}")


@dataclass(order=True)
class PrioritisedNode:
    priority: int
    node: Node = field(compare=False)


def get_h(src: Node, dst: Node) -> int:
    return abs(src.x - dst.x) + abs(src.y - dst.y)


def main():
    grid: List[List[Node]] = []

    with open("input15") as f:
        lines = f.readlines()

        for y in range(len(lines)):
            row: List[Node] = []
            for x in range(len(lines[y].rstrip("\n"))):
                new_node = Node(x, y, int(lines[y][x]))
                row.append(new_node)
            grid.append(row)

    source = grid[0][0]
    destination = grid[len(grid) - 1][len(grid[0]) - 1]

    source.g_val = 0
    source.h_val = get_h(source, destination)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x].h_val = get_h(grid[y][x], destination)
            if x > 0:
                grid[y][x].add_child(grid[y][x - 1])
            if x < len(grid[0]) - 1:
                grid[y][x].add_child(grid[y][x + 1])
            if y > 0:
                grid[y][x].add_child(grid[y - 1][x])
            if y < len(grid) - 1:
                grid[y][x].add_child(grid[y + 1][x])

    to_visit: List[PrioritisedNode] = []

    for neighbour in source.children:
        neighbour.visited_from = source
        neighbour.g_val = neighbour.risk
        heapq.heappush(to_visit, PrioritisedNode(priority=neighbour.f_val(), node=neighbour))

    while len(to_visit):
        if destination.visited_from:
            break

        current = heapq.heappop(to_visit).node

        for neighbour in current.children:
            if not neighbour.visited_from or neighbour.f_val() > current.g_val + neighbour.risk + neighbour.h_val:
                neighbour.visited_from = current
                neighbour.g_val = current.g_val + neighbour.risk
                if neighbour is destination:
                    break
                heapq.heappush(to_visit, PrioritisedNode(priority=neighbour.f_val(), node=neighbour))

    print(f"P1: {destination.g_val}")


if __name__ == "__main__":
    main()
