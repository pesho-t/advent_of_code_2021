from copy import deepcopy
import sys
from typing import Dict


class Node:
    def __init__(self, element: str):
        self.element = element
        self.next = None

    def insert(self, node) -> None:
        node.next = self.next
        self.next = node


def node_to_str(node: Node) -> str:
    printed = ""

    current = node
    while current:
        printed += current.element
        current = current.next

    return printed


def part_one(list_head: Node, rules_index: Dict[str, str], counts_index: Dict[str, int], its: int) -> int:
    counts_idx_copy = deepcopy(counts_index)

    for i in range(its):
        current = list_head
        while current.next:
            next_node = current.next
            element = rules_index.get(f"{current.element}{next_node.element}")
            if element:
                current.insert(Node(element))
                count = counts_idx_copy.setdefault(element, 0)
                count += 1
                counts_idx_copy[element] = count
            current = next_node
        print(f"After {i} iterations: {node_to_str(list_head)}")

    most_common = 0
    least_common = sys.maxsize
    for v in counts_idx_copy.values():
        most_common = max(most_common, v)
        least_common = min(least_common, v)

    return most_common - least_common


def part_two(list_head: Node, rules_index: Dict[str, str], counts_index: Dict[str, int], its: int) -> int:
    pair_index: Dict[str, int] = {}

    counts_idx_copy = deepcopy(counts_index)

    current = list_head
    while current.next:
        key = f"{current.element}{current.next.element}"
        count = pair_index.setdefault(key, 0)
        count += 1
        pair_index[key] = count
        current = current.next

    # We already did 10 in P1
    for i in range(its):
        new_pairs: Dict[str, int] = {}
        for pair, count in pair_index.items():

            to_insert = rules_index.get(pair)
            if to_insert:
                first = f"{pair[0]}{to_insert}"
                first_count = new_pairs.setdefault(first, 0)
                first_count += count
                new_pairs[first] = first_count

                second = f"{to_insert}{pair[1]}"
                second_count = new_pairs.setdefault(second, 0)
                second_count += count
                new_pairs[second] = second_count

                total_count = counts_idx_copy.setdefault(to_insert, 0)
                total_count += count
                counts_idx_copy[to_insert] = total_count

        pair_index = new_pairs

    most_common = 0
    least_common = sys.maxsize

    for v in counts_idx_copy.values():
        most_common = max(most_common, v)
        least_common = min(least_common, v)

    return most_common - least_common


def main():
    index: Dict[str, str] = {}

    with open("input14") as f:
        lines = f.readlines()

        template = lines.pop(0).rstrip("\n")
        lines.pop(0)  # get rid of the blank line

        for line in lines:
            pair, elem = line.rstrip("\n").split(" -> ")
            index[pair] = elem

    counts: Dict[str, int] = {}

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

    print(f"P1 --> {part_two(head, index, counts, 10)}")
    print(f"P2 --> {part_two(head, index, counts, 40)}")


if __name__ == "__main__":
    main()
