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

def create_plots(filename):
    prefix = filename.split("_")[0]
    data = get_file_data(filename)
    time = [dt.datetime.fromtimestamp(s) for s in data[:, 0]]

    headers = get_file_header(filename)
    filename_suffixes = [
            "temperature",
            "humidity",
            "pressure",
            "wind_direction",
            "wind_speed",
            "wind_gust",
            "solar_radiation",
            "battery_level"
            ]
    titles = [
            "{} Temperature".format(prefix),
            "{} Humidity".format(prefix),
            "{} Pressure".format(prefix),
            "{} Wind Direction".format(prefix),
            "{} Wind Speed".format(prefix),
            "{} Wind Gust".format(prefix),
            "{} Solar Radiation".format(prefix),
            "{} Battery Level".format(prefix)
            ]
    xlabels = [
            "Time (month-day hr)",
            "Time (month-day hr)",
            "Time (month-day hr)",
            "Wind Direction (degrees)",
            "Time (month-day hr)",
            "Time (month-day hr)",
            "Time (month-day hr)",
            "Time (month-day hr)"
            ]
    ylabels = [
            "Temperature (C)",
            "Humidity (%)",
            "Pressure (inHg)",
            "Frequency (counts)",
            "Wind Speed (m/s)",
            "Wind Gust (m/s)",
            "Solar Radiation (W/m^2 ?)",
            "Battery Level (W-hr)"
            ]

    for i in range(1, len(headers)):
        print("\tPlotting {}".format(headers[i]))

        if i == 4:
            plt.hist(data[:, i], bins=36)
        else:
            plt.plot(time, data[:, i])

        plt.title(titles[i-1])
        plt.ylabel(ylabels[i-1])
        plt.xlabel(xlabels[i-1])
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig("./figures/{}_{}.png".format(prefix, filename_suffixes[i-1]))
        plt.close()

def main():
    if not os.path.exists("./figures"):
        os.mkdir("./figures")

    for elem in sys.argv[1:]:
        print("Plotting {}...".format(elem))
        create_plots(elem)

if __name__ == "__main__":
    main()
