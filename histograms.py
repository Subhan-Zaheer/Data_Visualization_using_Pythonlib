import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

if __name__ == '__main__':
    iris_flower_df = sns.load_dataset('iris')

    plt.hist(iris_flower_df.sepal_width, bins=np.arange(2, 5, 0.25))

    #Multiple Histogram
    setosa_df = iris_flower_df[iris_flower_df['species'] == 'setosa']
    versicolor_df = iris_flower_df[iris_flower_df['species'] == 'versicolor']
    virginica_df = iris_flower_df[iris_flower_df['species'] == 'virginica']
    iris_flower_df.species.unique()
    plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
    plt.hist(virginica_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
    plt.legend(['setosa', 'viriginica']);

    #Multiple Histogram with stack over each other.
    plt.hist([setosa_df.sepal_width, virginica_df.sepal_width, versicolor_df.sepal_width], bins=np.arange(2, 5, 0.25),
             stacked=True)