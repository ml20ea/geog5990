# Import random module
import random

# Generate x0 and y0 at random locations on the grid
y0 = random.randint(0,99)
x0 = random.randint(0,99)

# Move x0 and y0 twice
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# Print the final position of x0, y0
print(y0, x0)

# Generate x1 and y1 at random locations on the grid
y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Move x1 and y1 twice
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# Print final position of x1, y1
print(y1, x1)

# Use Pythagores theorem to calculate the distance
answer = ( (x0-x1)**2 + (y0-y1)**2 ) ** 0.5

print(answer)