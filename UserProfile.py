class Profile:
    def __init__(self, username, age, location, numFlowers = 0, ):
        self._username = username #implement getters/setters (ability to change)
        self._age = age 
        self._location = location #implement getters/setters (ability to change)
        self._numFlowers = numFlowers #just set to 0 for now because the user will start w/ no flowers

    def get_username(self):
        return self._username
    
    #anything w/ change is basically a setter
    def change_username(self, newName):
        self._username = newName

    def get_age(self):
        return self._age
    
    def increment_age(self):
        self._age += 1

    def change_location(self, newLoc):
        self._location = newLoc

    def 