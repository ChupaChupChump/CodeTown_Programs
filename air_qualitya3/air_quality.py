#!/usr/bin/env python3

def read_data():
    readingsFile = open("readings.txt", "r")
    global readings
    readings = readingsFile.read()

read_data()
print(readings)