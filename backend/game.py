nameList = []

def setPlayersAmount():
    players = input("Set players amount:" )
    return int(players)
    


def setNames(playersamount):
    for x in range(1,playersamount+1):
        name = input("Set name " + str(x) + ": ")
        nameList.append(name)
    print(nameList)


setNames(setPlayersAmount())        