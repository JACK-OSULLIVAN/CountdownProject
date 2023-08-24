import itertools


TARGET = 264
FINAL_LIST = []

USER_LIST = [9, 10, 9, 1, 50, 25]



class NumberGame:
    def __init__(self, user_list):
        self.user_list = user_list
        self.next_depth_list(user_list)

    def next_depth_list(self, user_list):
        depth = 1
        next_list = []
        number_list = []
        for i in range(1, len(user_list)):
            possible_combs = list(itertools.combinations(user_list, i))
            next_list.extend(possible_combs)
        for i in range(0, len(next_list)):
            unique_number = Number(depth=1, input_tuple=next_list[i])
            number_list.append(unique_number)
        print(number_list)
        print(number_list[20].input_tuple)

number_game = NumberGame(USER_LIST)


class TupleCombination:
    def __init__(self, tuplecombination=()):
        self.tuple_combination = tuplecombination

    @property
    def tuple_combination(self):
        # print("Getting value...")
        return self._tuple_combination

    @tuple_combination.setter
    def tuple_combination(self, value):
        # print("Setting value...")
        if not isinstance(value, tuple):
            raise ValueError("Requires Tuple")
        self._tuple_combination = value


    @property
    def used_numbers(self):
        return self._used_numbers

    @used_number.setter
    def used_numbers(self):
        if not isinstance(value, int):
            raise ValueError("Must be integer")
        self._used_numbers = value



user_list = [9, 10, 9, 1, 50, 25]

# So first we need a function that generates all possible combinations into Tuples

next_list = []
for i in range(1, len(user_list) + 1):
    possible_combs = list(itertools.combinations(user_list, i))
    next_list.extend(possible_combs)

print(next_list)

# Assume these Tuples are similar to the numbers for Celsius, Pass in tuples to create new object

object_list = []

for t in next_list:
    tuple_object = TupleCombination(t)
    object_list.append(tuple_object)

print(object_list)

number_combinations = [tuple_object.tuple_combination for tuple_object in object_list]

print(number_combinations)
print(type(number_combinations[6][1]))
