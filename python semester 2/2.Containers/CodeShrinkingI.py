# Import modules
import random
import operator
import matplotlib.pyplot

# Create list named agents
agents = []

# Add x0, y0 to the list
agents.append([random.randint(0,99), random.randint(0,99)])

# Move x0 and y0 twice
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# Add x1, y1 to the list
agents.append([random.randint(0,99), random.randint(0,99)])

# Move x1 and y1 twice
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

# Print final position of the points
print(agents)

# Use Pythagores theorem to calculate the distance
answer = ( (agents[0][1]-agents[1][1])**2 + (agents[0][0]-agents[1][0])**2 ) ** 0.5

print(answer)

# Get maximum point based on x
print(max(agents, key=operator.itemgetter(1)))

# Plot the points to analyze them
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()