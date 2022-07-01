#!/usr/bin/python3

import random


total = 1000
success_count = 0

for _ in range(total):
    boxes = {}
    success = True
    
    # random box filling
    for i in range(1, 101):
        value = random.randint(1, 100)
        while value in boxes.values():
            value = random.randint(1, 100)
        else:
            boxes[i] = value


    for i in range(1, 101):
        count = 0
        found = False
        value = i
        while count < 50 and found == False:
            if boxes[value] == i:
                found = True
            else:
                value = boxes[value]

            count += 1

        if found == False:
            success = False
    if success:
        success_count += 1


print(f"Percentage: {(success_count / total) * 100: .2f}")

