from letter_game_class_list import CreateGameDict, ScoreGenerator
import random
import time

# Create a list of the alphabet
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet_list = [*alphabet]
ALPHABET_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # Create a separate vowel list and consonant list
# vowel = "aeiou"
# vowel_list = [letter for letter in ALPHABET_LIST if letter in vowel]
# consonant_list = [letter for letter in ALPHABET_LIST if letter not in vowel]
VOWEL_LIST = ['a', 'e', 'i', 'o', 'u']
CONSONANT_LIST = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


# TODO: Let the User Choose 9 letters, being either consonants or vowels
"""Currently commented out as I'm running randomly generated lists of different vowel-consonant ratios"""

#
# def user_choice():
#     count = 0
#     while count <= 8:
#         user_choice = input("consonant(c) or vowel(v)? ")
#         if user_choice == "c":
#             chosen_consonant = random.choice(CONSONANT_LIST)  # choice method is used assuming infinite number of each letter
#             user_list.append(chosen_consonant)
#             count += 1
#             print(f"Your current letters are: {user_list}\n"
#                   f"{9 - count} letters remaining.")
#         elif user_choice == "v":
#             chosen_vowel = random.choice(VOWEL_LIST)
#             user_list.append(chosen_vowel)
#             count += 1
#             print(f"Your current letters are: {user_list}\n"
#                   f"{9 - count} letters remaining.")
#         else:
#             "Incorrect input, please enter again"
#
# user_list =[]
# user_choice()
# print(user_list)


# TODO: Create a dataset for the different v:c combinations and determine the mean score for each combination


word_bank = CreateGameDict().generate_game_dict()

user_list = random.choices(VOWEL_LIST, k=4) + random.choices(CONSONANT_LIST, k=5)
print(user_list)

count = 0
score_list = []
start_time = time.time()

while count < 100:
    user_list = random.choices(VOWEL_LIST, k=4) + random.choices(CONSONANT_LIST, k=5)
    RepeatTest = ScoreGenerator(user_list=user_list, word_dict=word_bank)
    score_list.append(RepeatTest.score)
    count += 1

end_time = time.time()
time_taken = end_time - start_time

print(score_list)
print(f"It took {time_taken} seconds to complete {count} runs of the game")

# TODO: Need to account for None return (set to zero)
# TODO: Automate ratios (adjust the choices values)
# TODO: Export the data to a data text file where columns are ratio, and list. rows are list of each ratio
# TODO: Run stats on each dataset
# TODO: Make a Nominal Distribution Curve for each ratio.

# What would happen if choices was changed to sample? does this change ratios if each letter in list is unique

