import main
if __name__ == '__main__':
    iris_flower_df = main.sns.load_dataset('iris')
    print(iris_flower_df)
    main.mpl.rcParams['figure.figsize'] = (16, 12)
    main.plt.plot(iris_flower_df.sepal_length, iris_flower_df.sepal_width, marker='o', ls='')
    main.sns.scatterplot(iris_flower_df.sepal_length, iris_flower_df.sepal_width, iris_flower_df.species, s=400);
    pass

"""
If you have too much values in short range of values then you can use scatter-plot from seaborn lib.
Now, in above example we have three different species of flowers, so we change the color for every specie in graph using
hue parameter in scatter-plot.
"""