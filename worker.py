class Work:
    def __init__(self):
        pass

class Worker:
    def __init__(self,no):
        self.no = no
        self.work = None 
    
    def assign(self,work):
        self.work = work 

class Desk:
    def __init__(self,no):
        self.no = no
        self.weight = 0
        self.have = False
        self.meal = None
        self.assigned = False

    def update(self, weight):
        self.weight = weight
    
    def order(self, meal):
        self.meal = meal
        self.have = True 
    
    def clean(self):
        self.weight = 0
        self.have = False
        self.meal = None
        self.assigned = False

class Meals:
    def __init__(self,no,name):
        pass
