import itertools


TARGET = 264
FINAL_LIST = []

USER_LIST = [9, 10, 9, 1, 50, 25]

class Number:
    def __init__(self, input_tuple, depth):
        self.input_tuple = input_tuple
        self.depth = depth
        self.used_numbers = []

    def create_new_number(self, depth):
        new_depth = depth
        pass


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
