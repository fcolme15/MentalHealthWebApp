from random import randint #Random num generator
DrinkTask = [
    "Drink a glass of water",
    "Don't drink soda",
]
WalkingTask = [
    "Take a 10 minute walk!",
    "Take a 5 minute walk", 
    "Take a 15 minute walk"
]
EatingTask = [
    "Eat a fruit",
    "Plan your next meal",
    "Eat a cheat meal",
]
class Tasks():
    def __init__ (self):
        self.randomNum = [] #Array of rand nums
        self.map = {
            1 : "DrinkTask",
            2 : "WalkingTask",
            3 : "EatingTask"
        }
        


    def getRandom(self, loops = 5, highRange=8):
        for random in range (loops):
            result = randint(1,highRange) #random number 1-8
            self.randomNum.append(result)

    def GetTask(self):
        random = self.getRandom(1,len(self.map))
        return random[self.getRandom(1,len(DrinkTask))]

