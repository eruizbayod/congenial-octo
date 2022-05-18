#Implement a Caesar Cipher function that takes a string and shift amount, outputs the encrypted string.
#- Input: hello word
#- Shift by: 7
#- Output: olssv dvysk

count = 0
text = input ("Enter text: ")
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

if count == len(text):
    print("Please enter a text.")
    quit()

shift_amount = input ("Enter amount you want to shift the message:")

if not isinstance(int(shift_amount), int):
    print("Please, enter a valid number")
    quit()

shift_amount = int(shift_amount)

print(shift_amount)

for i in text:

    if i.islower():

        for x in range(0,26):

            if i == letters[x]:

                if (x+shift_amount) <= 25:
                            print(end = letters[x + shift_amount])

                else:
                            print(end = letters[x + shift_amount - 26])

    else:        

        for x in range(26, 52):

            if i == letters[x]:

                if (x + shift_amount) <= 51:
                            print(end = letters[shift_amount + x])

                else:
                            print(end = letters[(shift_amount+x) - 26])

    
