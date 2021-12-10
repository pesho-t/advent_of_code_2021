#!/usr/bin/env python3


def main():
    buckets = [0 for _ in range(9)]

    with open("input06") as f:
        age_line = f.readlines().pop().rstrip("\n")
        for age_str in age_line.split(","):
            age = int(age_str)
            buckets[age] += 1

    for day in range(256):
        spawning_fish = buckets.pop(0)

        buckets.append(spawning_fish)
        buckets[6] += spawning_fish

    total = 0

    for num in buckets:
        total += num

    print(total)


if __name__ == "__main__":
    main()
