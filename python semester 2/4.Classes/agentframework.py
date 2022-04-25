import random

class Agent():
    def __init__(self):
        self._x = random.randint(0, 99)
        self._y = random.randint(0, 99)
        
    def set_x(self, x):
        self._x = x
        
    def set_y(self, y):
        self._y = y
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100