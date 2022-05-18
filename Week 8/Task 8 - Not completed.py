from curses.ascii import isdigit
from operator import contains
import Levenshtein
import argparse
import sys
from string import punctuation

def getArgs():
    parser = argparse.ArgumentParser(description="Spell Checker")
    parser.add_argument("-i", "--input", help="input file", required = True)
    parser.add_argument("-o", "--outpot", help = "output file", required = True)
    parser.add_argument("-d", "--dictionary", help = "dictionary file", required= True)
    return parser.parse_args()

def fileToList(file):
    list = []
    with open(file, "r") as f:
        for line in f:
            list += line.split()
    return list


    

def main():

    args = getArgs()
    
    originalText = fileToList(args.input)
    dictionary = fileToList(args.dictionary)

    for word in originalText:
        
        if word isdigit:
            

    correctedText = []

    

    
    
    
    
    
    
    