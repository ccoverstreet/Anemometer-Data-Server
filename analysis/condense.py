import os
import sys
import numpy as np

def get_file_data(name):
    data = np.genfromtxt(name, delimiter=",", skip_header=1) 
    mask = data[:, 4] != np.NaN
    return data[mask, :]

def get_file_header(name):
    with open(name) as f:
        for line in f:
            return line

def main():
    files = os.listdir()
    files.sort()

    raw_data = []
    template_file = ""
    for name in files:
        if name.startswith(sys.argv[1]):
            template_file = name
            raw_data.append(get_file_data(name))

    stacked = np.vstack([data for data in raw_data])

    header = get_file_header(template_file)

    with open("condensed_{}.csv".format(sys.argv[1]), "w") as f:
        f.write(header)
        for data in stacked:
            i = 0
            for val in data:
                if i == 0:
                    f.write(str(int(val)))
                else:
                    f.write(",{}".format(str(val)))
                    
                i += 1



            f.write("\n")


if __name__ == "__main__":
    main()
