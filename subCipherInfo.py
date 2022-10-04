"""
@Author Reyce Salisbury
Information gathering of a ciphertext

Arg 1 can be a file path or a ciphertext.

if argument 1 is a path to a file:
    subCiperInfo will use the file to build the ciphertext

if arg 1 is ciphertext:
    subCipherInfo will use the given ciphertext
"""

import sys
from os.path import exists

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
AVG_ENG_PERCENTAGES = [
    ('E', 13.1), ('T', 9.23), ('A', 8.15), ('O', 7.76), ('I', 7.52), ('N', 6.8), ('S', 6.27), ('H', 6.1), 
    ('R', 6), ('D', 4.3), ('L', 4), ('C', 2.9), ('U', 2.8), ('M', 2.5), ('W', 2.4), ('F', 2.2), ('G', 2.1), 
    ('Y', 2), ('P', 1.9), ('B', 1.5), ('V', .98), ('K', .77), ('J', .15), ('X', .14), ('Q', .09), ('Z', 0.07)
    ]

def get_total_ctext(filename):
    total_text = ""
    with open(filename) as file:
        for line in file:
            total_text += str(line)
    return total_text

def get_info(cipher):
    print("Info for ciphertext:\n   |  char  | Total  |    %    |\tVisual\t   |  Average   | Suggested |")
    cipherList = [*cipher.lower().strip(" ")]
    totals = {'a':0, 'b':0,'c':0,'d':0,'e':0,'f':0, 'g':0, 'h':0,
    'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0,
     'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

    percentages = {'a':0.0, 'b':0.0,'c':0.0,'d':0.0,'e':0.0,'f':0.0, 'g':0.0, 'h':0.0,
    'i':0.0, 'j':0.0, 'k':0.0, 'l':0.0, 'm':0.0, 'n':0.0, 'o':0.0, 'p':0.0, 'q':0.0,
     'r':0.0, 's':0.0, 't':0.0, 'u':0.0, 'v':0.0, 'w':0.0, 'x':0.0, 'y':0.0, 'z':0.0}

    # get total number of x char in ciphertext
    for t in totals.keys():
        for s in cipherList:
            if (s == t):
                totals[t] += 1

    # get percentages of x char in ciphertext
    cipherLen = len(cipherList)
    for p in percentages.keys():
        percentages[p] = round(100 * totals[p] / cipherLen, 2)

    #convert dict into list of tuples for ordering
    percList = sort_tuple_list([(k, v) for k, v in percentages.items()])
    info = []
    for i in range(26):
        char = percList[i][0]
        amount = totals[char]
        percentage = percList[i][1]
        info.append((char, amount, percentage))

    # print percentages and totals for each char in human readable format, starting at the highest percent
    for i in range(len(percList)):
        if round(info[i][2]) > 0:
            visual = "*" * round(info[i][2]) + " " * (20 - round(info[i][2]))
        else:
            visual = " " * 20

        print( f"\t{info[i][0]}\t{info[i][1]}\t{info[i][2]}% \t {visual}" +
        f"{AVG_ENG_PERCENTAGES[i][0]} - {AVG_ENG_PERCENTAGES[i][1]}%\t  {info[i][0]} -> {AVG_ENG_PERCENTAGES[i][0]}")


# sorts a list of tuples by the greater second value
def sort_tuple_list(tupList):
     
    # getting length of list of tuples
    listLen = len(tupList)
    for i in range(0, listLen):
         
        for j in range(0, listLen-i-1):
            if (tupList[j][1] < tupList[j + 1][1]):
                temp = tupList[j]
                tupList[j] = tupList[j + 1]
                tupList[j + 1]= temp
    return tupList


# check all ranges of caesar cipher on ciphertext
def caesar_check(cipher):
    cipher = cipher.lower()
    print(f"Caesar options for cipher text below:\n\t{cipher}\n")
    for key in range(26):
        translated = ''
        for char in cipher:
            if char in LETTERS:
                num = ord(char)
                num = num - key
                if num < 96:
                    num = num + 26
                translated = translated + LETTERS[num - 96]
            else:
                translated = translated + char
        print(f"\t{translated}")


def main():
    if len(sys.argv) == 1:  # no ciphertext provided in args, ask for filename
        given = input("What is the ciphertext/filepath to ciphertext? >> ")
        
        if exists(given):
            print(f"\nUsing ciphertext from {given}\n")
            cipher = get_total_ctext(given)
        else:
            print("\nUsing ciphertext from input above.\n")
            cipher = given

    elif len(sys.argv) == 2:  # ciphertext provided in args
        if exists(sys.argv[1]):
            print(f"\nUsing ciphertext from {sys.argv[1]}\n")
            cipher = get_total_ctext(sys.argv[1])
            
        else:
            print("\nUsing ciphertext from argument input above.\n")
            cipher = sys.argv[1]
    else:
        raise(ValueError("Too many arguments! Call with a ciphertext argument, or a filepath argument."))
    
    caesar_check(cipher)
    print()
    get_info(cipher)


if __name__ == '__main__':
    main()
    