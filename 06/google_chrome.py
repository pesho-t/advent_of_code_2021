#!/usr/bin/env python3

"""
This will eat your RAM >:D
"""

from typing import Optional


class Fish:
    def __init__(self, starting_age: int):
        self.current_age = starting_age

    def tick(self) -> Optional:
        spawn_new_fish = False

        if self.current_age == 0:
            spawn_new_fish = True
            self.current_age = 6
        else:
            self.current_age -= 1

        if spawn_new_fish:
            return Fish(self.current_age + 2)


def main():
    fishies = list()

    with open("input06") as f:
        age_line = f.readlines().pop().rstrip("\n")
        for age in age_line.split(","):
            fishies.append(Fish(int(age)))

    for day in range(256):
        print(f"Day {day}")
        new_fish = list()

        for fish in fishies:
            spawned = fish.tick()

            if spawned:
                new_fish.append(spawned)

        fishies.extend(new_fish)

    print(len(fishies))


if __name__ == "__main__":
    main()
