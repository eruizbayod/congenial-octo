# Write a program that given a list of numbers, multiply all numbers in the list. Bonus for ignoring non-number element. Example: input: [1, 2, 3, 4], output: 24

list = [2, 3, 5, 10 ,3]
result = list[0]

for i in range(1, len(list)):
    result = result * list[i]

print(result)
 