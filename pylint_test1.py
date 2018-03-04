"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 Letter Shift)"""

import string

shift = 3
choice = input("Would you like to encode or decode?")
word = (input("Please Enter Text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == " ":
    for letter in word:
        if letter == " ":
            encoded = encoded + " "
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]

if choice == "decode":
    for letter in word:
        if letter == " ":
            encoded = encoded + " "
        else:
            x = letters.index(letter) - shift
            encoded = encoded + letters[x]

print(encoded)
