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
plt.legend() is also a function used when we have to plot multiple lines.  
plt.plot(marker) we can also add marker to our graph using this function.

plt.plot() also contain following parameters for styling and marker and any other things : 
1. color or c - used for coloring the line in graph.
2. linestyle or ls - used to choose between solid and dashed line.
3. linewidth or lw - used to set the width of line in graph.
4. marketsize or ms - used to set the size of marker.
5. markeredgecolor or mec - used to color the edge of marker.
6. markeredgewidth or mew - used to set the width of edge of marker.
7. markerfacecolor or mfc - set the fill colors for markers.
8. alpha - for the opacity of plot.

Shortly we can also add arguments shortly like:
    <[marker]><[line]><[color]>
 
"""