import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns


"""
A heat map is used to plot 2-dimensional data like a matrix or table using colors.
"""
if __name__ == '__main__':
    flights_df = sns.load_dataset('flights')
    plt.plot(flights_df.passengers)
    flights_df1 = flights_df.pivot('month', 'year', 'passengers')
    sns.heatmap(flights_df1)
    plt.title('Number of Passengers in 1000s')
    sns.heatmap(flights_df1, fmt='d', annot=True)