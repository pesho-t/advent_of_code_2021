#!/usr/bin/env python3


def o_or_x(val):
    return "x" if val else "o"


class Card:
    def __init__(self, lines):
        #print(f"parsing lines '{lines}'")
        #import pdb; pdb.set_trace()

        self.checks = [False for _ in range(25)]
        self.index = {}
        self.card = []
        self.unmarked_sum = 0

        pos = 0
        for line in lines:
            for num in line.rstrip("\n").split(" "):
                if num == " " or num == "":
                    continue
                self.index[num] = pos
                self.card.append(int(num))
                self.unmarked_sum += int(num)
                pos += 1
        # print(f"{self.index}")
        # print(f"{self.card}")
        # print(f"{self.unmarked_sum}")

    def mark_num(self, num):
        pos = self.index.get(num)
        if pos is not None:
            self.checks[pos] = True
            self.unmarked_sum -= int(num)

    def is_winning(self):
        # Check for winning rows
        for y in range(5):
            checks = 0
            for x in range(5):
                if self.checks[y * 5 + x]:
                    checks += 1
                else:
                    break
            if checks == 5:
                return True

        # Check for winning cols
        for x in range(5):
            checks = 0
            for y in range(5):
                if self.checks[y * 5 + x]:
                    checks += 1
                else:
                    break
            if checks == 5:
                return True

        return False

    def print(self):
        print("--------------------------")
        for x in range(5):
            print(f"{o_or_x(self.checks[x * 5 + 0])} {o_or_x(self.checks[x * 5 + 1])} {o_or_x(self.checks[x * 5 + 2])} {o_or_x(self.checks[x * 5 + 3])} {o_or_x(self.checks[x * 5 + 4])} | {self.card[x * 5 + 0]:2} {self.card[x * 5 + 1]:2} {self.card[x * 5 + 2]:2} {self.card[x * 5 + 3]:2} {self.card[x * 5 + 4]:2}")
        print("--------------------------")


def parse_cards(lines):
    cards = []
    while lines:
        to_parse = []
        for x in range(5):
            to_parse.append(lines.pop(0))
        if len(to_parse) != 5:
            raise ValueError("Bad lines")

        # print(f"Parsing {to_parse}")
        parsed = Card(to_parse)
        cards.append(parsed)
        if lines:
            lines.pop(0)  # Pop blank line

    return cards


def main():
    with open("input") as f:
        input_lines = f.readlines()
        drawn_string = input_lines.pop(0)
        drawn_nums = [num for num in drawn_string.rstrip("\n").split(",")]

        input_lines.pop(0)

        cards = parse_cards(input_lines)

        print(f"parsed {len(cards)} cards")

        winning_cards = []

        for num in drawn_nums:
            for x in range(len(cards)):

                if x in winning_cards:
                    continue

                cards[x].mark_num(num)

                if cards[x].is_winning():
                    winning_cards.append(x)
                    print(f"There are now {len(winning_cards)} winning cards")
                    if len(winning_cards) == len(cards):
                        print(f"{cards[x].unmarked_sum}, called: {num}")
                        return

        print("No winners??")


if __name__ == '__main__':
    main()
