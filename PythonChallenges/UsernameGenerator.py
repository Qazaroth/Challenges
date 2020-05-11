from urllib.request import urlopen
import random
from datetime import datetime

wordListSrc = "https://raw.githubusercontent.com/TTT2866/Batch-username-generator/master/wordlist.txt"
wordListTemp = urlopen(wordListSrc)
wordList = wordListTemp.read().__str__()

noOfUsernames = 1

random.seed(datetime.now())


def genUsername():
    usernames = ""

    for i in range(1, noOfUsernames + 1):
        firstName = newWordList[random.randint(0, newWordList.__len__())]
        secondName = newWordList[random.randint(0, newWordList.__len__())]

        randNo = random.randint(1, 999)

        if randNo < 10:
            randNo = str("00{r}".format(r=randNo))
        elif randNo < 90:
            randNo = str("0{r}".format(r=randNo))
        else:
            randNo = str(randNo)

        usernames = usernames + "\n{i} - {firstName}{secondName}{randNo}".format(i=i,
                                                                firstName=firstName.capitalize(),
                                                                secondName=secondName,
                                                                randNo=randNo)

    return usernames


noOfUsernames = input("How many usernames do you want to generate? ")

try:
    noOfUsernames = int(noOfUsernames)
except ValueError:
    print("Invalid no of usernames, defaulting to 1.")
    noOfUsernames = 1

#Checks if pyarmor is installed, since pyarmor makes it so that first 2 characters are b'
if wordList[0] == "b" and wordList[1] == "'":
    newWordList = wordList[2:].split('\\n')

    usernameTemp = genUsername()

    print(usernameTemp)
else:
    newWordList = wordList.split('\\n')

    usernameTemp = genUsername()

    print(usernameTemp)
