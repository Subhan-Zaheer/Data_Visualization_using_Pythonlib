import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
if __name__ == '__main__':
    ls = np.arange(1, 10)
    ls = np.random.permutation(ls)
    num = np.arange(1, 10)
    ls1 = np.arange(1, 10)
    ls1 = np.random.permutation(ls1)

    ##  Simple bar charts

    plt.bar(ls, num)
    plt.bar(ls1, num)
    plt.bar(ls, num)
    plt.bar(ls1, num, bottom=ls)
    plt.plot(ls1, num, 'o--r')
    plt.legend(['ls', 'ls1'])

    ##   Bar Charts of mean values

    tips_df = sns.load_dataset('tips')
    avg_bill_df = days = tips_df.groupby('day')[['total_bill']].sum()
    plt.bar(avg_bill_df.index, avg_bill_df.total_bill)
    plt.plot(avg_bill_df.index, avg_bill_df.total_bill, 'o--r')

    ##sns.barplot() will automatically calculate the mean of values.

    sns.barplot('day', 'total_bill', data=tips_df)
