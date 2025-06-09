from database import *
from player import *

players = []
categoryList = getCategories()
currentPlayer = Player("Mehdi", "Patata", "6")

player1 = Player("Prueba1", "Eurovision", "1")
player2 = Player("Prueba2", "Musica", "2")
player3 = Player("Prueba3", "Deporte", "3")
player4 = Player("Prueba4", "Colores", "4")
player5 = Player("Prueba5", "Animales", "5")

players.append(player1)
players.append(player2)
players.append(player3)
players.append(player4)
players.append(player5)



def setUpGame():
    players_amount = int(input("Set players amount: " ))
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
               
    for _ in range(players_amount):
      name = unique_name()
      category = valid_category(name)
      category_id = getCategoryId(category)
      player = Player(name, category, category_id)
      players.append(player)
      ##player.printvalues()
      ##player.getEasyQuestion()



def randomizer():
    global currentPlayer
    randomizer = random.randint(0, len(players)-1)
    print("Player choosen " +  players[randomizer].name)
    currentPlayer = players[randomizer]
    return players[randomizer]


def start():
    setUpGame()
    ##randomizer()
  
  

 

start()