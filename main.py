def howMany():
    return int(input("How many number would you like to enter? "))

def enterValue(nAvg):
    valueList = []
    for i in range(1, nAvg+1):
        valueList.append(int(input(str(i) + ": Please enter a number ")))
        print("You have entered " + str(valueList[i-1]))
    return valueList

def calAvg(vAvg):
    tmpAvg = 0
    for i in vAvg:
        tmpAvg += int(i)
    return tmpAvg/len(vAvg)

def main():
    nAvg = howMany()
    vAvg = enterValue(nAvg)
    print(calAvg(vAvg))

if __name__ == "__main__":
    main()