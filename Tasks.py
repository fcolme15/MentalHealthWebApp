from random import randint #Random num generator



class Task():
    def __init__ (self):
        self.randomNum = [] #Array of rand nums
        #variable of type string that holds what the task is 



    def getRandom(self, loops = 1, highRange=8):
        for random in range (loops):
            result = randint(1,highRange) #random number 1-8
            self.randomNum.append(result)

