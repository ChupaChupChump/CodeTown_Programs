#!/usr/bin/env python3

#air_quality programming task 2 by Mitchell Charity


import os
cwd = os.getcwd()

def read_data(filename):
    file = open(filename, "r")

    # Converting text file to a dicionary and seperating by ','
    data_dict = {}

    #Iterates over line in readings.txt and split each line where a ',' is
    #then strips '\n' from the lists in the dictionary
    #then converts to float and sppends to the dicitonary
    for line in file:
        location, reading_val = line.split(",")
        reading_val = reading_val.rstrip("\n")
        reading_val = float(reading_val)

        try:
            data_dict[location].append(reading_val)
        except KeyError:
            data_dict[location] = [reading_val]

    return data_dict

# Iterates over items in read_data function and adds them together to find the average
def get_average_dictionary(readings):
    avg_dict = {}
    for k, v in readings.items():
            
        avg_dict[k] = sum(v)/ float(len(v))
    
    return avg_dict
    
FILENAME = "readings.txt"

if __name__ == "__main__":
    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        #Loops through the keys in averages, sorted from that with the largest associated value in averages to the lowest - see https://docs.python.org/3.5/library/functions.html#sorted for details
        for location in sorted(averages, key = averages.get, reverse = True):
            print(location, averages[location])

    except (IOError, ValueError):
        print("Error reading {}".format(FILENAME))
        print("Please ensure the file exists and matches the required format")
        print("(each line should begin with a location name, followed by a comma, followed by an AQI reading)")