nameList = []

def setPlayersAmount(playersamount):
    return playersamount


def setNames(playersamount):
    for x in range(1,playersamount+1):
        name = input("Set name " + str(x) + ": ")
        nameList.append(name)
    print(nameList)




setNames(setPlayersAmount(5))        