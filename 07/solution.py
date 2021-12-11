from typing import List


def calc_fuel_cost(num_moves: int) -> int:
    total_cost = 0
    current_cost = 1

    while num_moves:
        total_cost += current_cost
        current_cost += 1
        num_moves -= 1

    return total_cost


def part_one(positions: List[int]) -> int:
    """
    As the cost of each move is constant, the alignment position
    is the median of the set
    """
    positions.sort()

    if len(positions) % 2 == 1:
        align_to = positions[int((len(positions) - 1)/2)]
    else:
        # If there isn't an absolute middle, pick the middle two numbers and choose
        # the one which is the furthest from the end of the list on its side.
        # I.e. [1, 2, 3, 10] -> middle = 2, 3 -> pick 3 as 10 - 3 > 2 - 1
        med_high = positions[int(len(positions)/2)]
        med_low = positions[int(len(positions)/2) - 1]

        if med_low - positions[0] > positions[len(positions)-1] - med_high:
            align_to = med_low
        else:
            align_to = med_high

    fuel_used = 0

    for pos in positions:
        fuel_used += abs(align_to - pos)

    return fuel_used


def part_two(positions: List[int]) -> int:
    """
    As the cost of each move is not constant, the alignment position
    is the average of the set
    """
    pos_sum = 0

    for pos in positions:
        pos_sum += pos
    ave = int(pos_sum / len(positions))

    fuel_used = 0
    for pos in positions:
        fuel_used += calc_fuel_cost(abs(ave - pos))

    return fuel_used


def main():
    positions = list()

    with open("input07") as f:
        pos_line = f.readlines().pop().rstrip("\n")
        for pos_str in pos_line.split(","):
            positions.append(int(pos_str))

    print(f"P1: {part_one(positions)}")
    print(f"P2: {part_two(positions)}")


if __name__ == "__main__":
    main()
