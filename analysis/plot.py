import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def get_file_data(name):
    data = np.genfromtxt(name, delimiter=",", skip_header=1) 
    mask = data[:, 4] != np.NaN
    return data[mask, :]

def get_file_header(name):
    with open(name) as f:
        for line in f:
            return line.split(",")

data = get_file_data(sys.argv[1])
time = [dt.datetime.fromtimestamp(s) for s in data[:, 0]]

headers = get_file_header(sys.argv[1])
ylabels = [
    "Temperature (C)",
    "Humidity (%)",
    "Pressure (inHg)",
    "Wind Direction (degrees)",
    "Wind Speed (m/s)",
    "Wind Gust (m/s)",
    "Solar Radiation (W/m^2 ?)",
    "Battery Level (W-hr)"
    ]

for i in range(1, len(headers)):
    print("Plotting {}".format(headers[i]))

    plt.plot(time, data[:, i])

    plt.ylabel(ylabels[i -1])
    plt.xlabel("Time (month-day hr)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


