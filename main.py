
def loadArray():
    num = input("What's the number? ")
    values = []

    while num != "":
        values.append(int(num))
        num = input("What's the number? ")
    return values

def findMin():
    return "Min"

def findMax():
    max = element[0]
    maxindex = 1
    i = 2
    while i < len(element):
        if element[i] > max:
            max = element[i]
            maxindex = i
        i = i + 1
    print(f"The highest value is {max} at position {maxindex}")

def findWord():
    data = input("Enter date (dd/mm/yy): ")
    startDays = 0
    startmonths = 3
    days = data[startDays:2]
    month = data[startmonths:startmonths+2]
    print(f"The month is {month} and the day is {days}")

def insertWord():
    og = input("What's your initial string? ")
    new = input("What's your new word? ")
    found = False
    i = 0
    while i < len(og) and found == False:
        checkLetter = og[i]
        if checkLetter == ";":
            first = og[0:i]
            second = og[i+1:len(og)-1]

        i = i + 1

def deleteWord():
    return

# element = loadArray()


choice = input("1: Find max\n2: Find min\n3:Words")
if choice == "1":
    findMax()
elif choice == "2":
    findMin()
elif choice =="3":
    opt = input("1: Find word\n2: Insert word\n3:Delete word")
    if opt == "1":
        findWord()
    elif opt == "2":
        insertWord()
    else:
        deleteWord()