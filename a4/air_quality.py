#!/usr/bin/env python3

import sys, time, os
import tkinter as tk

title = "Air Quality Assessor 3000"
author = "Mitchell Charity"

standard = {"o":8.0,"s": 20,"p": 25} # Dictionary for standard values


# I used seperate functions for each pollutant

def ozoneCheck(): # Ozone pollutant value checker
	while True:
		try:
			ozone = input("    Amount of Ozone record (parts per hundred million: ")
			global o # makes global variable
			o = float(ozone) # attempt to convert ot float

			while o < 0: #same as above but if negative
				o = input("    Enter a positive number: ") 
				o = float(o)
			break

		except (ValueError):
			pass

def sulfurDioxideCheck(): #Same as ozoneCheck() but for Sulfur Dioxide
	while True:
		try:
			sulfurDioxide = input("    Amount of sulfur dioxide record (parts per hundred million: ")
			global s
			s = float(sulfurDioxide)

			while s < 0:
				s = input("    Enter a positive number: ")
				s = float(s)
			break

		except (ValueError):
			print("    Not a number!")

def otherParticlesCheck():
	while True:
		try:
			otherParticles = input("    Amount of particles less than 2.5 micrometres diameter record (micrograms per cubic meter): ")
			global p
			p = float(otherParticles)

			while p < 0:
				p = input("    Enter a positive number: ")
				p = float(p)
			break

		except (ValueError):
			print("    Not a number!")

def reading():            
	while True:
		try:
			reading = input("Enter number of readings: ")
			global r
			r = int(reading)

			while r < 0:
				reading = input("Enter a positive number: ")
				r = int(reading)
			break

		except (ValueError, TypeError):
			print("Not a number!")


def largest(AQIA,a): 
  
    # Initialize maximum element 
    max = AQIA[0] 
  
    # Traverse array elements from second 
    # and compare every element with  
    # current max 
    for i in range(1, n): 
        if AQIA[i] > max: 
            max = AQIA[i] 
    return max
	
reading()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

global n
n = 0
while n < r:
	print("Reading", n+1)
	# Calling functions
	ozoneCheck()
	sulfurDioxideCheck()
	otherParticlesCheck()

	#printed to make sure they were the right value
	#print(o)
	#print(s)
	#print(p)

	# Calculating variables independently 
	# Results were tested to be exact to assessment exmaples
	AQIO =100 * ( o / standard["o"] )
	round(AQIO)
	AQIS = 100 * ( s / standard["s"] )
	round(AQIS)
	AQIP = 100 * ( p / standard["p"] )
	round(AQIP)

	AQIA = [AQIO, AQIS, AQIP] # Array of results of AQI for O, S & P
	a = len(AQIA) # Length of array AQIA into variable a
	AQI = largest(AQIA, a)  # Make largest number AQI
	print(" ") # Blank line 
	print("AQI: ",  AQI) 
	print(" ")
	n +=1


