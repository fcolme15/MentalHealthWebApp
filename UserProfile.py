

class Profile:
    def __init__(self, username, age, zipCode, numFlowers = 0, isFlowerDone = False, isCarryover = False):
        self._username = username #implement getters/setters (ability to change)
        self._age = age 
        self._zipCode = zipCode #implement getters/setters (ability to change)
        self.numFlowers = numFlowers #just set to 0 for now because the user will start w/ no flowers
        self._flowerStatus = isFlowerDone
        self.carryover = isCarryover #will be for checking if flower transfers to next day

    def get_username(self):
        return self._username
    
    #anything w/ change is basically a setter
    def change_username(self, newName):
        self._username = newName

    def get_age(self):
        return self._age
    
    #lowkey i might want to get rid of age class variable because we have to keep track
    #of birthday in order to increment it
    def increment_age(self): 
        self._age += 1

    def change_zip(self, newZip):
        self._zipCode = newZip

    def increment_flowers(self):
        self.numFlowers += 1

    def get_status(self):
        return self._flowerStatus

    def finish_flower(self): #will be used when a user finishes a flower
        self._flowerStatus = True

    def carry_flower(self): #will be used on days when self.get_status == false
        self.carryover = True 