inputCharacter = input("Input a character: ")

if inputCharacter.__len__() == 1:
    asciiVal = ord(inputCharacter)
    print(bin(asciiVal))
else:
    print("Expected a character, given a string of length more than 1.")
