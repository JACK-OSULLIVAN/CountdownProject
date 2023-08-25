import itertools


# Open and read  text file(downloaded from https://www.wordgamedictionary.com/enable/), contains ENABLE dict
class CreateGameDict:
    def __init__(self):
        self.game_dict = self.generate_game_dict()

    def generate_game_dict(self):
        with open("words.txt") as file:
            data = file.read()
        word_list = data.split()
        word_dict = {}
        for word in word_list:
            word_length = len(word)
            if word_length < 10:
                if word_length in word_dict:
                    word_dict[word_length].append(word)
                else:
                    word_dict[word_length] = [word]
        return word_dict




class ScoreGenerator:
    def __init__(self, user_list, word_dict):
        self.user_list = user_list
        self.user_dict = self.generate_user_dict()
        self.score = self.highest_score(word_dict=word_dict)

    # TODO: From user_list generate all possible permutations. Sort into Dictionary {Key=len(word): value=[perms of len(word)]}
    """ Note: I've done it this way to hopefully reduce time taken,
    will need to import time module to check (delete when tested)"""
    def generate_user_dict(self):
        user_dict = {}
        for i in range(1, len(self.user_list) + 1):
            possible_combs = list(itertools.permutations(self.user_list, i))  # For words, order of letters is important, therefore permutations instead of combinations
            possible_word_permutations = [''.join(tups) for tups in possible_combs]
            if i in user_dict:
                user_dict[i].extend(possible_word_permutations)
            else:
                user_dict[i] = possible_word_permutations
            self.user_dict = user_dict
        return self.user_dict

    # Starting from maximum length of word, cross-reference permutations with words from word_dict
    def highest_score(self, word_dict):
        for i in range(len(self.user_list), 1, -1):
            word_found = set(self.user_dict[i]).intersection(word_dict[i])
            if not word_found == set():
                score = int(i)
                words = set(self.user_dict[i]).intersection(word_dict[i])
                self.score = score
                return self.score

