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
    matplotlib.pyplot.imshow(environment)

f.close()
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
   

'''2. Set the parameters'''
num_of_agents=10
num_of_iterations=100


'''3. Make agents'''

agents=[]

'''4. Move the agents'''
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
    
    
''' Plot the agents'''  
matplotlib.pyplot.xlim(0,99) 
matplotlib.pyplot.ylim(0,99)  
 
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()
    