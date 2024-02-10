from random import randint #Random num generator

class Tasks():
    def __init__ (self):
        self.randomNum = [] #Array of rand nums



    def getRandom(self, loops = 5, highRange=8):
        for random in range (loops):
            result = randint(1,highRange) #random number 1-8
            self.randomNum.append(result)

