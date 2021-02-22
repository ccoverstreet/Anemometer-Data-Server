import matplotlib.pyplot as plt
import numpy as np
import sys

def main():
    print(sys.argv)
    if len(sys.argv) == 1:
       printHelp()
       return
    else:
        generatePlots(sys.argv[1:])

    
    
def printHelp():
    print("""QuickPlot for Anemometer Data
Usage:
    Provide a file/globbed files as an argument. This script will then generate a plot vs time for each parameter

Example:
    python quickplot.py mydatafile.csv
        or
    python3 quickplot.py mydatafile.csv""")

def generatePlots(filenames):
    time = []
    temp = []
    humidity = []
    pressure = []
    direction = []
    speed = []
    gust = []
    solar_rad = []
    bat_level = []

    for i in range(0, len(filenames)):
        with open(filenames[i]) as f:
            for line in f:
                if line.startswith("unixTime"):
                    continue

                split_line = line.split(",")
                time.append(float(split_line[0]) / 1000)
                temp.append(float(split_line[1]))
                humidity.append(float(split_line[2]))
                pressure.append(float(split_line[3]))
                direction.append(float(split_line[4]))
                speed.append(float(split_line[5]))
                gust.append(float(split_line[6]))
                solar_rad.append(float(split_line[7]))
                bat_level.append(float(split_line[8]))

    plt.plot(time, temp, "o")
    plt.title("Anemometer temperature")
    plt.ylabel("Temperature (C)")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()

    plt.plot(time, humidity, "o")
    plt.title("Anemometer humidity")
    plt.ylabel("%RH")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()

    plt.plot(time, pressure, "o")
    plt.title("Anemometer relative pressure")
    plt.ylabel("Pressure (in. of mercury)")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()

    plt.plot(time, direction, "o")
    plt.title("Anemometer wind direction")
    plt.ylabel("Degrees from N")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()

    plt.plot(time, speed, "o")
    plt.title("Anemometer wind speed")
    plt.ylabel("Wind Speed (m/s)")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()

    plt.plot(time, gust, "o")
    plt.title("Anemometer gust speed")
    plt.ylabel("Gust Speed (m/s)")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()

    plt.plot(time, solar_rad, "o")
    plt.title("Anemometer solar radiation")
    plt.ylabel("Need to verify units")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()

    plt.plot(time, bat_level, "o")
    plt.title("Anemometer battery level")
    plt.ylabel("Level (W-hr)")
    plt.xlabel("Time (seconds since Unix Epoch)")
    plt.show()


if __name__ == "__main__":
    main()
