from urllib.request import urlopen
import random
from datetime import datetime

wordListSrc = "https://raw.githubusercontent.com/TTT2866/Batch-username-generator/master/wordlist.txt"
wordListTemp = urlopen(wordListSrc)
wordList = wordListTemp.read().__str__()

random.seed(datetime.now())

if wordList[0] == "b" and wordList[1] == "'":
    newWordList = wordList[2:].split('\\n')

    firstName = newWordList[random.randint(0, newWordList.__len__())]
    secondName = newWordList[random.randint(0, newWordList.__len__())]

    randNo = random.randint(1, 999)

    if randNo < 10:
        randNo = str("00{r}".format(r=randNo))
    elif randNo < 90:
        randNo = str("0{r}".format(r=randNo))
    else:
        randNo = str(randNo)

    usernameTemp = "{firstName}{secondName}{randNo}".format(firstName=firstName.capitalize(),
                                                            secondName=secondName,
                                                            randNo=randNo)

    print(usernameTemp)
else:
    print("no")
