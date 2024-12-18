import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def my_func(a, b):
    array_of_numbers = np.random.normal(size=(a, b))
    df = pd.DataFrame(array_of_numbers)
    print(df.head())


def my_func2(c, d):
    result = pd.DataFrame(dict(ficrst_column=c, second_column=d))
    print(result.head())


def my_func3(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='^')
    ax.plot(x * 3, y, marker='*')
    ax.plot(2 * x, y, marker='+')
    plt.show()


a = 3
b = 5
c = [22, 33, 44, 55]
d = [66, 77, 88, 99]
x = np.array([-3, -2, -1, 0, 1, 2, 3])
y = np.array([9, 4, 1, 0, 1, 4, 9])

my_func(a, b)
my_func2(c, d)
my_func3(x, y)
