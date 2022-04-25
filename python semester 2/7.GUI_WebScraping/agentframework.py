import random

class Agent():
    def __init__(self, environment, agents, y, x):
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x 
        
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y 
    
        self.environment = environment
        self.store = 0 # We'll come to this in a second. 
        self.agents = agents
        
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
            
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10 
    
    def distance_between(self, agent):
        return (((self.get_x() - agent.get_x())**2) + 
                ((self.get_y() - agent.get_y())**2))**0.5
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                # This agent is a neighbour
                store = self.store + agent.store
                average = store / 2
                self.store = average
                agent.store = average