class Player:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    def printvalues(self):
        print("Hi i am " + self.name + " and my category is " +  self.category)




mehdi = Player("Mehdi", "Euroviiisut")

mehdi.printvalues()
