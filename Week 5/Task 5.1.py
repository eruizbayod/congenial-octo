# Make a program that uses a lookup table to convert any set of alphabets into their corresponding NATO phonetic alphabets. Also implement the inverse function.
# - Input: cat
# - Output: charlie alfa tango



natoAlph = {"a": "Alpha", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo", "f": "Foxtrot". "g": "golf", "h"= "Hotel", "i": "India", "j": "Juliett", "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o": "Oscar", "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango", "u": "Uniform", "w": "Whiskey", "x": "X-ray", "y": "Yankee", "z": "Zulu"}

def toNato():
    word = (input (str('Enter a word to convert to NATO phonetic alphabet:')))
    for letter in word:
        for key, value in natoAlph.items():
            if letter in key:
                print(value, end = " ")

def fromNato():
    word = (input (str('Enter a word to convert to NATO phonetic alphabet:')))
    setWord = word.split()

    for i in setWord:
        print(setWord[1])

