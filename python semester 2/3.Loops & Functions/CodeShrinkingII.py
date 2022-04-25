'''
    author = Enas
    date: 22/4
'''

# Import modules
import random
import operator
import matplotlib.pyplot
import time

def distance_between(agents_row_a, agents_row_b):
    distance = ((agents_row_a[1]-agents_row_b[1])**2 + 
                (agents_row_a[0]-agents_row_b[0])**2    ) ** 0.5

    return distance

num_of_agents = 10

# Create list named agents
agents = []

# Use loop to create number of agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99), random.randint(0,99)])

# Move each agent twice
for i in range(num_of_agents):
    for j in range(2):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# Print final position of the points
print(agents)

start = time.process_time()

max_distance = 0
min_distance = 150 # Maximum possible distance in our grid

# Use Pythagores theorem to calculate the distance
for i in range(num_of_agents):
    for j in range(i+1, num_of_agents):
        answer = distance_between(agents[i], agents[j])
        
        if answer > max_distance:
            max_distance = answer
            
        if answer < min_distance:
            min_distance = answer 

end = time.process_time()

print("Total time required =", (end-start) )

print("Maximum distance =", max_distance)
print("Minimum distance", min_distance)

# Get maximum point based on x
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# Plot all agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

# Plot the largest agent in red
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()