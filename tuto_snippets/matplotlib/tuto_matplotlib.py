# Install matplotlib
# pip install matplotlib pandas
# sudo apt install python3-tk

# Example 1: line plot
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

###########################

# Example 2: scatter plot

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

###########################

# Example 3: combined

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

###########################

# Example 4: csv pandas

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
df.head()

fig, ax = plt.subplots()
ax.plot(df.AAPL_x, df.AAPL_y)
ax.set(xlabel="Time (days)", ylabel="Price ($)", title='Apple Share Prices over time (2014)')
ax.grid(which="major", alpha=0.5)

plt.xticks(rotation="vertical")
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange( start, end, 7.0 ))
plt.show()

