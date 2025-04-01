players = []
categoryList = []
from database import *
from player import *

def setPlayersAmount():
    players = input("Set players amount: " )
    return int(players)
    
def getListCategories(list):
    for x in list:
        categoryList.append(x)
        


def setUpGame(playeramount):
    
    names = []
    
    def unique_name():
        while True:
           print("")
           name = input(f"Set name  {len(names)+1} : ")
           if name not in names:
               names.append(name)
               return name
           print("Name exists, choose another name")

    def valid_category(name):
        while True:
           print(categoryList)
           category = input("Choose category for " + name + ": ")
           if category in categoryList:
              categoryList.remove(category)
              return category

           print("Category incorrect, choose again")
               
    for _ in range(playeramount):
      name = unique_name()
      category = valid_category(name)
      player = Player(name, category)
      players.append(player)
      player.printvalues()

   
        
   
def start():
    getListCategories(getCategories())
    setUpGame(setPlayersAmount())

 

start()