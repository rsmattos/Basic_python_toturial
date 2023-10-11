#!/usr/bin/env python3

import matplotlib.pyplot as plt


def read_data(filename):
    """
    Opens the file passed, that should be in the format
    time    pop1    pop2

    Parameters
    ----------
    filename : str
        Name of the file with the populations

    Returns
    -------
    tuple(list, list, list)
        time, population 1 and population 2 read from the file
    """

    time = []
    pop1 = []
    pop2 = []

    with open(filename) as file:
        lines = file.readlines()

        for line in lines[1:]:
            words = line.split()

            time.append(float(words[0]))
            pop1.append(float(words[1]))
            pop2.append(float(words[2]))

    return time, pop1, pop2


def plot_populations(time, pop1, pop2):
    """
    From the time and populations passed, generate the plot and
    save to population_plot.png.

    Parameters
    ----------
    time : list
        Time series, x_range of the plot
    pop1 : list
        Population of state 1
    pop2 : list
        Population of state 2
    """
    
    plt.plot(time, pop1, label='State 1')
    plt.plot(time, pop2, label='State 2')
    plt.legend()
    plt.title('Populations')
    plt.xlabel('Time (fs)')
    plt.savefig('population_plot.png')
    return


if __name__ == '__main__':
    time, pop1, pop2 = read_data('data/populations.dat')
    plot_populations(time, pop1, pop2)