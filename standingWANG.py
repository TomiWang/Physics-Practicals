# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:03:17 2025

@author: Tomi Wang
"""

# Importing modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Defining sineWaveZeroPhi function
def sineWaveZeroPhi(x, t, k, w):
    return np.sin(k * x - w * t)

# Defining init function
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Independent variable
x = np.linspace(0, 10, 1000)

# Define animate function
def animate(i):
    t = 0.01 * i  # Time
    k = np.pi / 2  # Wave number

    # Dependent variable lists
    y1 = sineWaveZeroPhi(x, t, k, 2 * np.pi)
    y2 = sineWaveZeroPhi(x, t, k, -2 * np.pi)
    y3 = y1 + y2  # Sum of y1 and y2 for standing wave

    # Combined it into a 2D list for easier access
    waveFunctions = [[x, y1], [x, y2], [x, y3]]

    # Updated each line using waveFunctions
    for j in range(len(lines)):
        lines[j].set_data(waveFunctions[j][0], waveFunctions[j][1])

    return lines

# Set up the figure and axes
fig = plt.figure()
subplot = plt.axes(xlim=(0, 10), xlabel="x", ylim=(-2, 2), ylabel="y")
line1, = subplot.plot([], [], lw=2)
line2, = subplot.plot([], [], lw=2)
line3, = subplot.plot([], [], lw=2)
lines = [line1, line2, line3]

# Create the animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Display the animation :)
plt.show()