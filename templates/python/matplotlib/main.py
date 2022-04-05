'''
Docs for Matplotlib module: https://matplotlib.org/stable/index.html
First make sure to run 'pip install -r requirements.txt'
'''
import matplotlib.pyplot as plt
import numpy as np

x_values = np.arange(0,10)
y_values = np.array([219, 215, 223, 210, 222, 239, 231, 237, 244, 236])

plt.plot(x_values, y_values)

plt.title("Title of my graph")

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid()

plt.xticks(x_values)
plt.yticks(y_values)

plt.show()