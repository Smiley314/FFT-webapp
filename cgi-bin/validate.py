#! /Users/melissabenefer/PycharmProjects/Test/venv/bin/python

import csv
import math
import os
from scipy import fftpack
import matplotlib.pyplot as plt


def gen_fft(filename):
    data = []

    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Specify the path to the input file
    input_file = os.path.join(home_dir, "PycharmProjects/FFT/webapp/data/", str(filename))
    with open(input_file) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0])

    real = []
    ima = []
    are = []
    count = 0
    freq = []


    # Get the frequency for the data points assuming equal time step
    freq = fftpack.fftfreq(len(data))

    # pass the vol data stored to the fft to compute the dft and store in the varaible "c"
    c = fftpack.fft(data)
    # Pass the dft data stored in "c" to the ifft module to compute the idft and store it in the varaible "q"
    q = fftpack.ifft(c)

    # calculate A = sqrt(real^ + ima^2) and sotre it as "are" (ploting are gives the same plot as dft
    for i in c:
        real.append(i.real)
        ima.append(i.imag)
        are.append(math.sqrt((i.real ** 2) + (i.imag ** 2)))

    # create figure with 2 subplots, dft and idft for comparing
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(abs(c))
    ax1.set_title('DFT')
    ax1.set(xlabel='Frequency', ylabel='Power')
    ax2.plot(q)
    ax2.set_title("IDFT")
    ax2.set(xlabel='Time', ylabel='Volts')
    fig.subplots_adjust(hspace=0.5, wspace=0.5)

    # Specify the path to the output directory and create it if it doesn't exist
    output_dir = os.path.join(home_dir, "PycharmProjects/FFT/webapp/data/")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot in the output directory
    filename = os.path.join(output_dir, "new_fig.png")
    plt.savefig(filename)





