import random
wordlist = []
wordlist = "aliakbar", "asghar", "mehdi"
word = ""


class HangmanGame:

    def __init__(self):
        self.__rand_word = random.choice(wordlist)
        self.__guess_left = 8

    def starmaker(self):
        stars = ""
        wordlen = len(self.__rand_word)
        for i in range(wordlen):
            stars += "*"
        return stars

    def game_status(self):
        if self.__guess_left == 0:
            print("you loose")

        elif "*" not in lstar:
            print("you won")
            exit()

    def games(self):
        for bb in range(self.__guess_left):
            x = input("guess: ")
            indices = [i for i, char in enumerate(word) if char == x]
            if indices == []:
                self.__guess_left -= 1
                game_status(self)
        print(guess_remain)
    for bb in indices:
        lstar[bb] = x
    print(lstar)
