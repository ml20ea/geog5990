# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:32:43 2022

@author: ml20ea
"""
import random
import matplotlib.pyplot
import operator
import csv
import agentframework 
import matplotlib.animation



'''1. Read in the in.txt and append to environment'''
f=open('python.txt', newline='')
reader=csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)


environment=[]
#Lines here happen before any data is processed
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
