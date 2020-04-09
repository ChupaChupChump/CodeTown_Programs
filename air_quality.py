#!/usr/bin/env python3

import sys, time, os

standard = {"o":1,"s": 2,"p": 3}

title = "Air Quality Assessor 3000"
author = "Mitchell Charity"

message = "Welcome to " + title
def typerWriter(message): # Fancy text
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)

typerWriter(message)
print(" ") #Make a empty space to make text pretty

def ozoneCheck():
	while True:
		try:
			ozone = input("Amount of Ozone record (parts per hundred million: ")
			global o
			o = float(ozone)

			while o < 0:
				o = input("Enter a positive number: ")
				o = float(o)
			break

		except (ValueError):
			print("Not a number!")

def sulfurDioxideCheck():
	while True:
		try:
			sulfurDioxide = input("Amount of sulfur dioxide record (parts per hundred million: ")
			global s
			s = float(sulfurDioxide)

			while s < 0:
				s = input("Enter a positive number: ")
				s = float(s)
			break

		except (ValueError):
			print("Not a number!")

def otherParticlesCheck():
	while True:
		try:
			otherParticles = input("Amount of particles less than 2.5 micrometres diameter record (micrograms per cubic meter): ")
			global p
			p = float(otherParticles)

			while p < 0:
				p = input("Enter a positive number: ")
				p = float(p)
			break

		except (ValueError):
			print("Not a number!")

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

	
reading()

global n
n = 0
while n < r:
	print("Reading", n+1)
	ozoneCheck()
	sulfurDioxideCheck()
	otherParticlesCheck()
	print(o)
	print(s)
	print(p)
	AQI = 100*(o + s + p)/(standard["o"]+standard["s"]+standard["p"]) 
	str(AQI)
	print("ÄQI: ",  AQI)
	n +=1

message = "Thank you for using " + title + ", made by " + author
typerWriter(message)
print(" ")