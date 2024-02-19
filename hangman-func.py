import random
wordlist = []
wordlist = "aliakbar", "asghar", "mehdi"
word = ""


def word_chooser():
    return random.choice(wordlist)
    # print(word)


word = word_chooser()

print(word)


def starmaker():
    stars = ""
    wordlen = len(word)
    for i in range(wordlen):
        stars += "*"
    return stars


xstar = starmaker()
guess_remain = 8


def game_status():
    if guess_remain == 0:
        print("you loose")
    else:
        if "*" not in lstar:
            print("you won")
            exit()


lstar = list(xstar)
for bb in range(guess_remain):
    x = input("guess: ")
    indices = [i for i, char in enumerate(word) if char == x]
    if indices == []:
        guess_remain -= 1
        game_status()
        print(guess_remain)
    for bb in indices:
        lstar[bb] = x
    print(lstar)

    game_status()
    # if "*" not in lstar:
    #     print("you won")


# starsstr = ""
# starlist = list(stars)
# for w in range(guess_remain):
#     x = input("Guess a letter: ")
#     if x in list(dictlist[0]):
#         indices = [i for i, char in enumerate(dictlist[0]) if char == x]
#         lenind= iny(len(indices))
#         for b in range(lenind):

#         xxx = dictlist[0].index(x)

#         starlist[xxx] = x
#         starsstr = "".join(starlist)
#         print(starsstr)
