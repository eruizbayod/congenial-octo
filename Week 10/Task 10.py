import random

faces = int(input("How many sides on the dice?"))
num_dices = int(input("How many dices"))
num_rolls = int(input("How many rolls for each dice?"))
total = 0

for i in range(num_rolls):

    for j in range(num_dices):
        roll = 0
        roll = random.randint(1, faces)
        print(f"Dice number {j+1} on the roll number {i+1}: {roll}")
        total += roll

print(f"The sum of all your dice rolls is: {total}")