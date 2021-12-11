#!/usr/bin/env python3

from typing import Dict, FrozenSet, List, Tuple


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    split = line.split(" | ")
    parsed_signals = split[0]
    parsed_displays = split[1]

    return parsed_signals.split(" "), parsed_displays.split(" ")


def parse_line_part_one(line: str) -> Dict[int, List[str]]:
    _, parsed_displays = parse_line(line)

    displays: Dict[int, List[str]] = dict()

    for display in parsed_displays:
        entries = displays.setdefault(len(display), list())
        entries.append(display)

    return displays


def parse_line_part_two(line: str) -> Tuple[Dict[int, List[FrozenSet[str]]], List[FrozenSet[str]]]:
    parsed_signals, parsed_displays = parse_line(line)

    signals: Dict[int, List[FrozenSet[str]]] = dict()
    displays: List[FrozenSet[str]] = list()

    for signal in parsed_signals:
        entries = signals.setdefault(len(signal), list())
        entries.append(frozenset({x for x in signal}))

    for display in parsed_displays:
        displays.append(frozenset({x for x in display}))

    return signals, displays


def part_one(lines: List[str]) -> int:
    """
    len(1) == 2
    len(4) == 4
    len(7) == 3
    len(8) == 7
    """
    accepted_lengths = {2, 4, 3, 7}  # 1, 4, 7, 8

    count = 0

    for line in lines:
        displays = parse_line_part_one(line.rstrip("\n"))

        for display_length, display_values in displays.items():
            if display_length in accepted_lengths:
                count += len(display_values)

    return count


def part_two(lines: List[str]) -> int:
    """
    len(0) == 6
    len(1) == 2
    len(2) == 5
    len(3) == 5
    len(4) == 4
    len(5) == 5
    len(6) == 6
    len(7) == 3
    len(8) == 7
    len(9) == 6
    """
    count = 0

    for line in lines:
        signals, displays = parse_line_part_two(line.rstrip("\n"))
        one = signals.get(2)[0]
        four = signals.get(4)[0]
        seven = signals.get(3)[0]
        eight = signals.get(7)[0]

        signal_to_int = {
            one: 1,
            four: 4,
            seven: 7,
            eight: 8
        }

        int_to_signal = {
            1: one,
            4: four,
            7: seven,
            8: eight
        }

        for six_long in signals.get(6):
            difference = six_long - one
            if len(difference) == 5:
                definitely_six = six_long
                signal_to_int[definitely_six] = 6
                int_to_signal[6] = definitely_six
                signals.get(6).remove(definitely_six)
                break

        for zero_or_nine in signals.get(6):
            difference = zero_or_nine - (seven.union(four))
            if len(difference) == 1:
                digit = 9
            else:
                digit = 0
            signal_to_int[zero_or_nine] = digit
            int_to_signal[digit] = zero_or_nine

        for five_long in signals.get(5):
            difference = five_long - seven
            if len(difference) == 2:
                definitely_three = five_long
                signal_to_int[definitely_three] = 3
                int_to_signal[3] = definitely_three
                signals.get(5).remove(definitely_three)
                break

        for five_or_two in signals.get(5):
            difference = five_or_two - int_to_signal[9]
            if len(difference) == 0:
                digit = 5
            else:
                digit = 2
            signal_to_int[five_or_two] = digit
            int_to_signal[digit] = five_or_two

        assert len(signal_to_int.keys()) == 10

        showing = (
            f"{signal_to_int[displays[0]]}"
            f"{signal_to_int[displays[1]]}"
            f"{signal_to_int[displays[2]]}"
            f"{signal_to_int[displays[3]]}"
        )
        count += int(showing)

    return count


def main():
    with open("input08") as f:
        lines = f.readlines()
        print(f"P1: {part_one(lines)}")
        print(f"P2: {part_two(lines)}")


if __name__ == "__main__":
    main()
