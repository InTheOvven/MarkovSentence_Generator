import random

def main():
    #Input
    pathToFile = input("Enter the path of the input file: ")
    wordList = GetInput(pathToFile)


    #Dict key(string) value(list str)
    wordDict = CreateDict(wordList)

    #Input 2 words to start generation/how many words should generate
    startingPair = input("Enter two words to start the word generation process: ")
    totalWords = GetTotalWords()

    #Generate the statement
    startingList = startingPair.split()
    listLength = len(startingList)
    outputList = []
    if startingList[listLength-2] + " " + startingList[listLength-1] in wordDict:
        word1 = startingList[listLength-2]
        word2 = startingList[listLength-1]
        outputList.append(word1)
        outputList.append(word2)
        for _ in range(totalWords):
            word3 = Generate(word1, word2, wordDict)
            outputList.append(word3)
            word1 = word2
            word2 = word3
    else:
        #For Later.... Implement auto restart
        print("The words you entered are not in the dictionary, please restart and try again.")

    #Output our generated text

    for word in outputList:
        print(word + " ", end="")


def Generate(sword1, sword2, wordDict):
    wordsPossible = wordDict[sword1 + " " + sword2]
    randomNumber = random.randint(0, len(wordsPossible) - 1)
    return wordsPossible[randomNumber]

def GetTotalWords():
    try:
        totalWords = input("Enter the total number of words to generate: ")
        totalWords = int(totalWords)
        return totalWords
    except:
        print("Please enter an integer!")
        GetTotalWords()

def CreateDict(wordList):
    i = 0
    word1 = ""
    word2 = ""
    word3 = ""
    wordDict = {}

    for word in wordList:
        if i == 0:
            word1 = word
        elif i == 1:
            word2 = word
        elif i == 2:
            word3 = word
        else:
            word1 = word2
            word2 = word3
            word3 = word

        if i > 2:
            if word1 + " " + word2 in wordDict:
                wordDict[word1 + " " + word2].append(word3)
            else:
                wordDict[word1 + " " + word2] = [word3]
        i = i + 1

    return wordDict



def GetInput(inputFile):
    with open(inputFile, 'r') as input:
        inputString= input.read()
        inputStringList = inputString.split()
        return inputStringList

main()