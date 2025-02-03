# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:46:40 2025

@author: Tomi Wang
"""

# Importing modules :D
from numpy import *
import matplotlib.pyplot as plt

# Function definition for sineWaveZero
def sineWaveZero(A, omega, t):
    return A * sin(-omega * t)

# Run test to see if function works
A = 1        # Amplitude
omega = 2    # Angular frequency
t_test = 1   # Time
print(sineWaveZero(A, omega, t_test))  # Example test

# Wave plot
dt = 0.01  # Step difference
t = arange(0, 2, dt)  # Independent variable (time values)
y1 = sineWaveZero(1, 2, t)  # First sine wave
y2 = sineWaveZero(1, 3, t)  # Second sine wave

# Adding the waves to show interference
y_interference = y1 + y2

# Graph plots
plt.plot(t, y1, label="Wave 1")
plt.plot(t, y2, label="Wave 2")
plt.plot(t, y_interference, label="Interference", linestyle="--")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.title("Wave Interference")
plt.legend()
plt.grid()
plt.show()

# Created independent variable list 't' with step difference of 0.1
dt = 0.1
t = arange(0, 100, dt)

# Created two dependent variable lists using sineWaveZero function
A = 1  # Amplitude
omega1 = 4.0  # Frequency for the first wave
omega2 = 4.3  # Frequency for the second wave

y1 = sineWaveZero(A, omega1, t)  # First sine wave
y2 = sineWaveZero(A, omega2, t)  # Second sine wave

# Create a plot figure
fig = plt.figure()

# Addd subplot that takes up the entire figure
subplot = fig.add_subplot(111)

# Plot the first sine wave
subplot.plot(t, y1, label="Wave 1 (4.0 rad/s)")

# Plot the second sine wave
subplot.plot(t, y2, label="Wave 2 (4.3 rad/s)")

# Plot the sum of two waves (interference)
y_sum = y1 + y2  # Element-wise sum
subplot.plot(t, y_sum, label="Sum of Waves (Beat Pattern)", linestyle="--")

# Added labels, title, and legend
subplot.set_xlabel("Time (t)")
subplot.set_ylabel("Amplitude")
subplot.set_title("Wave Interference and Beat Pattern")
subplot.legend()

# Show the plot :)
plt.show()