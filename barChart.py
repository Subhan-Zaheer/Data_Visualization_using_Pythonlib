import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    ls = np.arange(1, 10)
    ls = np.random.permutation(ls)
    num = np.arange(1, 10)
    ls1 = np.arange(1, 10)
    ls1 = np.random.permutation(ls1)
    plt.bar(ls, num)
    plt.bar(ls1, num)
    plt.bar(ls, num)
    plt.bar(ls1, num, bottom=ls)
    plt.plot(ls1, num, 'o--r')
    plt.legend(['ls', 'ls1'])