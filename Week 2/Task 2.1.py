a = 1
b = 10
c = 2
sum = 0

for i in range(a+1, b):
    if i % c == 0:
        sum += i

print(sum)