import random


class HangmanGame:

    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.word = self.word_chooser()
        self.stars = self.starmaker()
        self.guess_remain = 8
        self.lstar = list(self.stars)

    def word_chooser(self):
        return random.choice(self.wordlist)

    def starmaker(self):
        stars = ""
        wordlen = len(self.word)
        for i in range(wordlen):
            stars += "*"
        return stars

    def game_status(self):
        if self.guess_remain == 0:
            print("& you loose")

        elif "*" not in self.lstar:
            print("you won")
            exit()

    def play(self):
        while self.guess_remain > 0:
            x = input("guess: ")
            indices = [i for i, char in enumerate(self.word) if char == x]
            if indices == []:
                self.guess_remain -= 1

                print("you have only ", self.guess_remain, " guess")
                self.game_status()
            else:

                for bb in indices:
                    self.lstar[bb] = x
                print(self.lstar)
                self.game_status()


wordlist = ["aliakbar", "asghar", "mehdi", "ghazal", "setare"]
game = HangmanGame(wordlist)
while True:
    order = input("What you want to do? \norder: ")

    if order == "start":
        game.play()

    elif order == "exit":
        break

# game.play()
