import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv

%matplotlib qt

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.get_x() - agents_row_b.get_x())**2) +
    ((agents_row_a.get_y() - agents_row_b.get_y())**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

agents = []

environment = []

carry_on = True

with open("in.txt") as file:
    for row in csv.reader(file):
        rowlist = []
        for value in row:
            int_value = int(value)
            rowlist.append(int_value)
        environment.append(rowlist)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Prove that agents can see each other
print(agents[9].get_x(), agents[9].get_y())
print(agents[0].agents[9].get_x(), agents[0].agents[9].get_y())


def update(frame_number):
    global carry_on
    
    # Variable to hold all grass eaten by agents
    total_store = 0
    
    fig.clear() 
    
    # Move the agents.
    # Shuffle the agents at each iteration to remove artefacts
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        total_store += agents[i].store

    if total_store > 10000:
        # Agents have eaten a lot of the environement! Stopping condition
        carry_on = False
        print("Stopping condition")
    
    matplotlib.pyplot.xlim(0,99) 
    matplotlib.pyplot.ylim(0,99)  
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].get_x(), agents[i].get_y())


def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 