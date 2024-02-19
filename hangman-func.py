dictlist = []
dictlist = "aliakbar", "asghar"

print(len(dictlist[0]))
guess = len(dictlist[0])
stars = ""
for i in range(guess):
    stars += "*"

x0 = "b"
xx = dictlist[0].index(x0)
starlist = list(stars)
starlist[xx] = x0
starsstr = "".join(starlist)


# x0 = input()
# xx = dictlist[0].index(x0)
# if xx != None:
#     stars.index[xx] = x0
