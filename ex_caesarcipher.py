# Heavily inspired form https://gist.github.com/AO8/17fd55f8512af389245b41f7144a8270
# Written by AO8

# string is a convenient package to work with strings
import string
# time will allow us to wait for a few seconds
from time import sleep

# Check that user is running this with python3 and not python2
# package sys is convenient for such things
import sys
# if python version is inferior to 2, print a message saying we need python3
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


# store "abcdefghijklmnopqrstuvwxyz" in var alphabet as a string
alphabet = string.ascii_lowercase 
    
print("Welcome to Caesar Cipher Encryption.\n")
# Store the user's message in var message as lower case characters
message = input("Type a message you would like to encrypt: ").lower()
# Emty line
print()
# Store the user's key (shift) in var key as an integer (it has to be)
key = int(input("Enter your key: "))
# Create empty var encrypted_message
encrypted_message = ""

# Go through characters in the user's message
for c in message:
    # for each character in the message, we check if the character is also
    # in or alphabet string
    if c in alphabet:
        # We get the position of the character from the message in the alphabet
        # See: https://www.tutorialspoint.com/python/string_find.htm
        position = alphabet.find(c)
        # We add the key to the position of the character from the message in the alphabet
        # and store the remainder of the euclidian division of position + key in var new_position
        new_position = (position + key) % 26
        # we get the character from the alphabet which is at position of the remainder we just got
        new_character = alphabet[new_position]
        # we add the encrypted character to the string encrypted_message which is empty at first
        encrypted_message += new_character
    else:
        # if the character is not in the alphabet, we dont encrypt it and simply add it as is to the 
        # encrypted_message
        encrypted_message += c

# \n means line break
print("\nEncrypting your message...\n")
# give an appearance of doing something complicated
sleep(2) 
print("Stand by, almost finished...\n")
# more of the same
sleep(2) 
print("Your encrypted message is:\n")
print(encrypted_message)