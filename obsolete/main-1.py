import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define a function that generates data for multiple y-coordinates
def generate_data():
    t = 0
    while True:
        # Generate data for multiple y-coordinates
        y1 = np.sin(t)
        y2 = np.cos(t)
        y3 = np.sin(2 * t)
        
        # Yield a tuple of values for each y-coordinate
        yield y1, y2, y3
        
        t += 0.1  # Increment the time variable

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize empty plots for each y-coordinate
line1, = ax.plot([], [], label='y1')
line2, = ax.plot([], [], label='y2')
line3, = ax.plot([], [], label='y3')

# Define the initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

# Define the update function
def update(data):
    y1, y2, y3 = data
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    return line1, line2, line3

# Create x values for the plot
x = np.linspace(0, 2 * np.pi, 100)

# Create the animation
ani = FuncAnimation(fig, update, frames=generate_data, init_func=init, blit=True)

# Show the legend
ax.legend()

# Display the animation
plt.show()
