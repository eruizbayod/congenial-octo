sent = "blabla bla bla ble"
abc = "abcdefghijklmnopqrstuvwyz"
sum = 0

for i in (abc):
    for j in (sent):
        if i == j:
            sum = sum + 1
    print (i, ":", sum)
    sum=0