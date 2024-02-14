import random

def buildGrid():
    #add random numbers to our 2D array
    #2d array access must use NESTED loops

    for row in range(5):
        for col in range(5):
            #print(f"{row},{col}:{grid[row][col]}")
            grid[row][col] = getUnique()
    print(grid)
    return True

def printGrid():
    print("Print grid")
    return True

def clearFlags():
    print("Clear flags")
    return True

def play():
    return True

def getUnique():
    num = random.randint(1, 75)
    #num-1 is used because index in flags starts from 0
    while flags[num-1] != 0:
        num = random.randint(1,75)
    return num

#initialise 2D grid
grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
flags = []
for i in range(75):
    flags.append(0)
print(flags)

buildGrid()
printGrid()
clearFlags()
play()