import os

# Write string to file, then automaticaly close the file
def writeToFile(filename, string):
    with open(filename, mode="w") as myFile:
        myFile.write(string)

def appendToFile(filename, string):
    with open(filename, mode="a") as myFile:
        myFile.write(string)

def readWholeFileAsString(filename):
    with open(filename) as myFile:
        return myFile.read()   # returns 1 string

def readAllLinesFromFile(filename):
    with open(filename) as myFile:
        return myFile.readlines();  # returns a list of string

writeToFile("abc.txt", "string to save\n")
writeToFile("def.txt", "string to save\n")
appendToFile("abc.txt", "more text\n")
appendToFile("def.txt", "more text\n")
appendToFile("def.txt", "even more text\n")

print( "[" + readWholeFileAsString("def.txt") + "]" )
print( readAllLinesFromFile("def.txt") )   # ['string to save\n', 'more text\n', 'even more text\n']
