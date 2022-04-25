# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 04:32:26 2022

@author: 44770
"""
import random
import operator
import matplotlib.pyplot
import matplotlib.animation 

num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


ax.set_autoscale_on(False)

#Make the agents.
 
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

carry_on = True	
import random 


class Agent():
    
    def __init__(self, environment, agents):
        self.environment = environment
        self.agents=agents
        self.store = 0 # We'll come to this in a second. 
        self.x=random.randint(0,99)
        self.y=random.randint(0,99)
        print("x="+str(self.x)+", y="+str(self.y))
        
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0]  = (agents[i][0] + 1) % 99 
        else:
            agents[i][0]  = (agents[i][0] - 1) % 99
        
        if random.random() < 0.5:
            agents[i][1]  = (agents[i][1] + 1) % 99 
        else:
            agents[i][1]  = (agents[i][1] - 1) % 99 
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        #print(agents[i][0],agents[i][1])

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.xlim(0,99) 
matplotlib.pyplot.ylim(0,99)  
#matplotlib.pyplot.imshow(environment)
 
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1    
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()



matplotlib.pyplot.show()














