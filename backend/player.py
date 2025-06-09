from database import *

class Player:
    def __init__(self, name, category, category_id):
        self.name = name
        self.category = category
        self.category_id = category_id


    def printvalues(self):
        print("Hi i am " + self.name + " and my category is " +  self.category + " and my id is " + str(self.category_id))
     
    
    def getEasyQuestion(self):
        response = getQuestion(self.category_id, "easy")
        print(response)
        


