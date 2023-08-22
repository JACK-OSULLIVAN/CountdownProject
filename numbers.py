import math
import random

# Numbers Round. The contestant in control chooses six of 24 shuffled face-down number tiles, arranged into two groups:
# 20 "small numbers" (two each of 1 to 10) and four "large numbers" of 25, 50, 75 and 100.
# Random number is then generated

small_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
large_numbers = [25, 50, 75, 100]


n_small = int(input("How many small numbers? "))
n_large = int(input("How many large numbers? "))

user_list = random.sample(small_numbers, k=n_small) + random.sample(large_numbers, k=n_large)
print(user_list)

target = random.randint(101, 999)
print(target)


# Can use + - * and /(as long as %0)

import itertools
user_list = [9, 10, 9, 1, 50, 25]
target = 264

# Thinking best way atm would be to iterate through list, generating every possible positive integer via + - * /
# Draw a diagram
# For each new number generated, store two numbers used (can't be used again)

# Maybe first attempt just generate every combination, then filter

add_list =[]

for i in range(1, len(user_list)):
    possible_combs = list(itertools.combinations(user_list, i))
    add_list.extend(possible_combs)
    # print(len(possible_combs))
#
# print(add_list)
# print(len(add_list))

final_add_list = []
for index in add_list:
    new_value = sum(index)
    final_add_list.append(new_value)


unique_addition_numbers = list(set(final_add_list))
print(unique_addition_numbers)
