#!/usr/bin/env python3

import os
cwd = os.getcwd()


def read_data(filename):
    os.open(filename)
    return print(filename)

def get_average_dictionary(readings):
    pass  # TODO: Implement this correctly

FILENAME = "readings.txt"

if __name__ == "__main__":
    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        # Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest - see https://docs.python.org/3.5/library/functions.html#sorted for details
        for location in sorted(averages, key = averages.get, reverse = True):
            print(location, averages[location])

    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a location name, followed by a comma, followed by an AQI reading)")