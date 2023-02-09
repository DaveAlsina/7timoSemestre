from copy import deepcopy
import numpy as np
from matplotlib import pyplot as plt

# difference equation

def f(x, mu):
    return mu*x*(1 -x)

def run_f(x, mu, ntimes):
    
    xnew = x
    output = np.zeros(ntimes)
    output[0] = xnew

    for n in range(1, ntimes):
        xnew = f(xnew, mu)
        output[n] = xnew

    return output


def plot(xs, mus, ntimes):

    count = 0
    number_of_plots_per_subplot = 3
    number_of_subplots = int(len(xs)/number_of_plots_per_subplot)

    fig, axs = plt.subplots(number_of_subplots)
    fig.suptitle('Plot of mu variations')
    lines = [':', '-.', '-']

    count = [c for c in range(len(xs))]
    column = [c % number_of_plots_per_subplot for c in count]
    curr_subplot  = [int(c/number_of_plots_per_subplot) for c in count]

    for x, mu, c, col in zip(xs, mus, count, column):

        curr = curr_subplot[c]
        axs[curr].plot(run_f(x, mu, ntimes), linestyle = lines[col], label = f"mu = {mu}")
        axs[curr].legend()

    plt.show()


#build a function which makes subplots given some input
#INPUT: (list of outputs to plot on each subplot)

mus = [0.8, 1.3, 2.7, 3.46, 3.7, 3.95797]
xs  = [1/2]*len(mus)

plot(xs, mus, 40)



