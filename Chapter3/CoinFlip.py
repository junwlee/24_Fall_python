import random

coin = random.randrange(2)
pick = int(input("Write a number between 0 or 1: "))
chance = 0
while True:
    if pick == coin:
        print("You won!")
        chance += 1
        break
    else:
        print("You lost!")
        chance += 1

print("You won", chance, "")