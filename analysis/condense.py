import sys
import numpy as np
import os

def getHeader(filename):
    with open("{}/{}".format(sys.argv[1], filename)) as f:
        for line in f:
            return line

def gatherData(filenames, prefix):
    data = []
    header = getHeader(filenames[0])
    for filename in filenames:
        arr = np.genfromtxt("{}/{}".format(sys.argv[1], filename),
            skip_header=1,
            delimiter=",")
        if np.ndim(arr) != 2:
            continue

        data.append(arr)

    out = np.concatenate(data)
    mask = np.logical_not((np.isnan(out[:, 4])))
    out = out[mask, :]

    with open("{}_condensed.csv".format(prefix), "w") as f:
        f.write(header)

        for row in out:
            row.tofile(f, sep=",")
            f.write("\n")

def main():
    filenames = os.listdir(sys.argv[1])
    filenames.sort()

    cur_anemometer = filenames[0].split("-")[0]
    cur_filenames = []
    for filename in filenames:
        prefix = filename.split("-")[0]
        if prefix != cur_anemometer:
            gatherData(cur_filenames, cur_anemometer)
            cur_anemometer = prefix
            cur_filenames = []

        cur_filenames.append(filename)

    gatherData(cur_filenames, cur_anemometer) 
    

if __name__ == "__main__":
    main()
