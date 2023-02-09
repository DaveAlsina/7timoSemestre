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

    for x, mu in zip(xs, mus):

        if (count % number_of_plots_per_subplot==0):
            legends = []

            if count>0:
                axs[int(count/number_of_plots_per_subplot)].legend(legend)
                legends = []

        axs[int(count/3)].plot(run_f(x, mu, ntimes))
        legends.append(f"mu = {mu}")
        count += 1

    plt.show()



#build a function which makes subplots given some input
#INPUT: (list of outputs to plot on each subplot)

mus = [0.8, 1.3, 2.7, 3.46, 3.7, 3.95797]
xs  = [1/2]*len(mus)

plot(xs, mus, 40)



