from random import randint #Random num generator

class Tasks():
    def __init__ (self):
        self.randomNum = [] #Array of rand nums



    def getRandom(self):
        for random in range (7):
            result = randint(1,8) #random number 1-8
            self.randomNum.append(result)

