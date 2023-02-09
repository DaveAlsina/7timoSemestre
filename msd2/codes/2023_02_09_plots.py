from matplotlib import pyplot as plt

# difference equation

def f(x, mu):
    return mu*x*(1 -x)

def run_f(x, mu, ntimes):


#build a function which makes subplots given some input
#INPUT: (list of outputs to plot on each subplot)
