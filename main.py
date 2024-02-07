
def loadArray():
    num = input("What's the number? ")
    elements = []

    while num != "":
        elements.append(int(num))
        num = input("What's the number? ")
    return elements

def findMin():
    return "Min"

def findMax():
    return "Max"

values = loadArray()

choice = input("1: Find max\n2: Find min\n")
if choice == "1":
    findMax()
elif choice == "2":
    findMin()