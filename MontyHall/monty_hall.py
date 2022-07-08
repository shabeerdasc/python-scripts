#!/bin/python3

import random


def host_reveal(doors, pick):
    goats = []
    for i in range(3):
        if i == pick:
            continue
        if doors[i] == "goat":
            goats.append(i)
    if len(goats) > 1:
        return random.choice(goats)
    else:
        return goats[0]


def switch_choice(pick, host_choice, doors):
    switch = 3 - (pick + host_choice)
    return doors[switch]

doors = ["goat", "goat", "car"]


def main():
    win = 0
    win_without_switch = 0
    total = 100000
    for i in range(total):
        random.shuffle(doors)

        pick = random.choice(range(3))
        host_choice = host_reveal(doors, pick)
        switch = switch_choice(pick, host_choice, doors)
        if switch == "car":
            win += 1
        if doors[pick] == "car":
            win_without_switch += 1

    print("Win percentage with switch")
    percentage = (win / total) * 100
    print(f"Percentage win: {percentage}")

    print("Win percentage without switch")
    percentage = (win_without_switch / total) * 100
    print(f"Percentage win: {percentage}")


if __name__ == "__main__":
    main()

