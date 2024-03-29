# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository. 
#
#Delete these comments before commit!
#Good luck.

def onChange(event, car):
	if event != onChange.lastEvent:
		print(car.wheelAngle, car.speed)
		onChange.lastEvent = event
onChange.lastEvent = "START THE CAR"

class Event:
	eventType = ""
	value = 0

	def __init__():
		print(this.eventType)

class Car:
	wheelAngle = 0
	speed = 0
	maxSteeringAngle = 450
	minSteeringAngle = -450

	def act (self, event):
		eventType = event.eventType

		if eventType == "SPEED UP":
			speedUp(event.value)
		elif eventType == "SLOW DOWN":
			slowDown(event.value)
		elif eventType == "TURN":
			turnSteeringWheel(event.value)
	
	def speedUp (value):
		speed += value
	
	def slowDown (value):
		speed -= value
	
	def turnSteeringWheel (value):
		newValue = wheelAngle + value
		if  minSteeringAngle  <= newValue <= maxSteeringAngle:
			wheelAngle = newValue

car1 = Car()
event = Event

while event.eventType is not "END":
	car1.act(event)
	onChange(event.eventType, car1)
