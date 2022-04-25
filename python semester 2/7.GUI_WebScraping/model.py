import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import tkinter

import bs4
import requests

# Send request to the server
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')

# Fetch x and y data from the website
td_ys = soup.find_all(class_="y")
td_xs = soup.find_all(class_="x")

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
    # Set y and x to null if there are not enough values
    try:
        y = int(td_ys[i].text)
    except IndexError:
        y = None
        
    try:
        x = int(td_xs[i].text)
    except IndexError:
        x = None
        
    agents.append(agentframework.Agent(environment, agents, y, x)) 

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

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
root = tkinter.Tk() 
root.wm_title("Model")
menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal") 

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 


tkinter.mainloop()