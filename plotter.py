import matplotlib.pyplot as plt
import numpy as np


def BarGraphFromData(categories, values):
    # make the plot
    plt.bar(categories, values, color='skyblue', edgecolor='black',
            width=0.3)
    plt.title('Scores by Model')
    plt.xlabel('Model')
    plt.ylabel('Score')

    # display Gui
    plt.show()


# test data
#categories = ['A', 'B', 'C']
#values = [2, 2, 4]

#BarGraphFromData(categories, values)
