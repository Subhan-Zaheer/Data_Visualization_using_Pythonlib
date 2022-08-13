from matplotlib import pyplot as plt
import numpy as np
if __name__ == '__main__':
    x = (np.linspace(0, 10, 1000))
    print(x)
    y =  np.sin(x)
    print(y)
    plt.plot(x, y);


"""
Data Visualization is a graphical representation of data .It includes images to communicate relationships among the 
represented data to viewers.
We will be using MATPLOTLIB and SEABORN libraries for data visualization.

.plot() function in pyplot is used to draw a graph of data.
plt.xlabel, plt.ylabel are used to name the x-axis and y-axis of graph.
"""