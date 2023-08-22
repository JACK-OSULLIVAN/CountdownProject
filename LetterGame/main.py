import random
import itertools

# Letter Game
# Create a list of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = [*alphabet]  #Learnt this on stackoverflow, gamechanger!

# Create a separate vowel list and consonant list
vowel = "aeiou"
vowel_list = [letter for letter in alphabet_list if letter in vowel]
consonant_list = [letter for letter in alphabet_list if letter not in vowel]

# Let the User Choose 9 letters, being either consonants or vowels
COUNT = 0

def user_choice():
    global COUNT
    while COUNT <= 8:
        user_choice = input("consonant(c) or vowel(v)? ")
        if user_choice == "c":
            chosen_consonant = random.choice(consonant_list)  # choice method is used assuming infinite number of each letter
            user_list.append(chosen_consonant)
            COUNT += 1
            print(f"Your current letters are: {user_list}\n"
                  f"{9 - COUNT} letters remaining.")
        elif user_choice == "v":
            chosen_vowel = random.choice(vowel_list)
            user_list.append(chosen_vowel)
            COUNT += 1
            print(f"Your current letters are: {user_list}\n"
                  f"{9 - COUNT} letters remaining.")
        else:
            "Incorrect input, please enter again"


user_list = []
user_choice()

# From user_list generate all possible permutations. Sort into a Dictionary where Key = length of the word
# and value is a list of all permutations with that length.
""" Note: I've done it this way to hopefully reduce time taken, 
will need to import time module to check (delete when tested)"""

user_dict = {}
for i in range(1, len(user_list) + 1):
    possible_combs = list(itertools.permutations(user_list, i))  # For words, order of letters is important, therefore permutations instead of combinations
    possible_word_permutations = [''.join(tups) for tups in possible_combs]
    if i in user_dict:
        user_dict[i].extend(possible_word_permutations)
    else:
        user_dict[i] = possible_word_permutations

# Open and read the text file (downloaded from https://www.wordgamedictionary.com/enable/)
# that contains the ENABLE Dictionary.
with open("./words.txt") as file:
    data = file.read()

# Get all the words into a list
word_list = data.split()

# Sort the word list into a dictionary key=word_length: value=list of words with word length
word_dict = {}
for word in word_list:
    word_length = len(word)  # Note can start at words with length 10 later as larger words not needed
    if word_length in word_dict:
        word_dict[word_length].append(word)
    else:
        word_dict[word_length] = [word]

# Starting from maximum length of word, cross-reference permutations with words from word_dict
"""Currently set to print word length and every word available whilst testing.
Once satisfied will change it to stop at first key match"""

for i in range(len(user_list), 1, -1):
    try:
        print(i, set(user_dict[i]).intersection(word_dict[i]))
    except KeyError:  #
        print(f"there are no words present with length {i}")


# When looking at user_dict[i], obvious word raze was not found. something is wrong with the combination
# answer, had it set as combination instead of permutation

# Extra things I want to do on the project:
# Determine the optimal amount of vowels and consonants to choose to achieve average highest score
