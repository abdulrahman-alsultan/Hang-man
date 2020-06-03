import random
from Project3 import Man


def randNumber(x):
    return random.randint(0, x)


words = ["abruptly", "askew", "beekeeper", "boggle", "curacao", "buzzing", "buzzwords", "gazebo","eeeeeeeeeeeeeee"]
i = 10
word = words[randNumber(len(words)-1)]
under = "_" * len(word)
find = 0
while i > 0:
    if find == len(under):
        break
    print("Guess the word :", under)
    l = input()
    if l in word:
        index =0
        for q in word:
            if q ==l:
                under = list(under)
                if under[index] == '_':
                    under[index] = l
                    find += 1
            index+=1
        under = "".join(under)
    else:
        Man.draw(i)
        i-=1

if find == len(under):
    print("the word is : ",under)
    print("good work ^_^")