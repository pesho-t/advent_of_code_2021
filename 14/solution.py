import sys
from typing import Dict

class Node:
    def __init__(self, element: str):
        self.element = element
        self.next = None

    def insert(self, node) -> None:
        node.next = self.next
        self.next = node


def main():
    template = ""
    index: Dict[str, str] = {}
    counts: Dict[str, int] = {}

    with open("input14") as f:
        lines = f.readlines()

        template = lines.pop(0).rstrip("\n")
        lines.pop(0)  # get rid of the blank line

        for line in lines:
            pair, elem = line.rstrip("\n").split(" -> ")
            index[pair] = elem

    head = Node(template[0])
    counts[template[0]] = 1
    tail = head

    for i in range(1, len(template)):
        new_node = Node(template[i])
        tail.insert(new_node)
        tail = new_node
        count = counts.setdefault(template[i], 0)
        count += 1
        counts[template[i]] = count

    # Part 1
    for i in range(10):
        current = head
        while current.next:
            next_node = current.next
            element = index.get(f"{current.element}{next_node.element}")
            if element:
                current.insert(Node(element))
                count = counts.setdefault(element, 0)
                count += 1
                counts[element] = count
            current = next_node

    most_common = 0
    least_common = sys.maxsize
    for v in counts.values():
        most_common = max(most_common, v)
        least_common = min(least_common, v)

    print(f"P1 --> {most_common} - {least_common} = {most_common - least_common}")


if __name__ == "__main__":
    main()