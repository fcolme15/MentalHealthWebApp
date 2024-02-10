

class Flower():
    def __init__ (self, date, tasks, color):
        self._dateAcquired = date #string
        self._tasksCompleted = tasks #list of objects type Task
        self._flowerColor = color #string

    @property
    def get_acquired_date(self):
        return self._dateAcquired
    
    @property
    def retrieve_tasks(self):
        return self._tasksCompleted
    
    @property
    def get_color(self):
        return self._flowerColor