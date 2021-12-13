#!/usr/bin/env python3

from typing import Dict, Set


class Node:
    def __init__(self, name: str):
        self.name = name
        self.big = False
        self.adjacent: Set[Node] = set()

        if name.upper() == name:
            self.big = True

    def add_adjacent(self, node):
        self.adjacent.add(node)

    def __repr__(self):
        neighbours = ",".join([x.name for x in self.adjacent])
        return (
            f"{self.name}: {'is ' if self.big else 'not '}big. Neighbours: {neighbours}"
        )


def search(node: Node, visited: Set[Node] = None) -> int:
    if not visited:
        visited = set()

    if node.name == "end":
        return 1

    if not node.big and node in visited:
        return 0

    visited.add(node)

    num_paths = 0
    for neighbour in node.adjacent:
        num_paths += search(neighbour, visited)

    visited.discard(node)

    return num_paths


def main():
    index: Dict[str, Node] = dict()

    with open("input12") as f:
        lines = f.readlines()

        for line in lines:
            entries = line.rstrip("\n").split("-")

            if "start" in entries:
                entries.remove("start")
                name = entries.pop()
                node = index.setdefault(name, Node(name))
                start = index.setdefault("start", Node("start"))
                start.add_adjacent(node)
                continue

            if "end" in entries:
                entries.remove("end")
                name = entries.pop()
                node = index.setdefault(name, Node(name))
                end = index.setdefault("end", Node("end"))
                node.add_adjacent(end)
                continue

            first_name = entries[0]
            second_name = entries[1]

            node_one = index.setdefault(first_name, Node(first_name))
            node_two = index.setdefault(second_name, Node(second_name))

            node_one.add_adjacent(node_two)
            node_two.add_adjacent(node_one)

        num_paths = search(index["start"])

        print(num_paths)


if __name__ == "__main__":
    main()
