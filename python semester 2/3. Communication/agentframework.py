# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:35:21 2022

@author: ml20ea
"""

import random

y0 = 50
x0 = 50

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)

#Note that we can't do this:

if random.random() < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1

import matplotlib.pyplot
import matplotlib.animation 

num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
#plotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations) 


#ax.set_autoscale_on(False)

 #Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()
import random
import matplotlib.pyplot
#import operator
import csv
import agentframework 
import matplotlib.animation



'''1. Read in the in.txt and append to environment'''
f=open('python.txt', newline='')
reader=csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)


environment=[]
# Lines here happen before any data is processed
for row in reader:
    rowlist=[]
    for value in row:
         rowlist.append(value)
    environment.append(rowlist)




'''2. Set the parameters'''
num_of_agents=10
num_of_iterations=100
neighbourhood=20

carry_on=True
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


'''3. Make agents'''

agents=[]

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


    
'''4. Move the agents'''

	
def update(frame_number):
    global carry_on
    fig.clear()   
    #for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    matplotlib.pyplot.xlim(0,99) 
    matplotlib.pyplot.ylim(0,99)  
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    


    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1    
'''animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)'''

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
''''animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)'''
matplotlib.pyplot.show()
import random
#import operator
import matplotlib.pyplot
import matplotlib.animation 

num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
#plotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations) 


ax.set_autoscale_on(False)

 #Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

matplotlib.pyplot.show()
import random

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
        print(agents[i][0],agents[i][1])

		
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
matplotlib.pyplot.imshow(environment)
 
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























