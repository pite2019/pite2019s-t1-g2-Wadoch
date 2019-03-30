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

class Event:
	def __init__(self):
		self.event_type = ""

	def detect_event_by_key_press(self, key):
		if key == "w":
			self.event_type = "SPEED UP"
		elif key == "s":
			self.event_type = "SLOW DOWN"
		elif key == "a":
			self.event_type = "TURN LEFT"
		elif key == "d":
			self.event_type = "TURN RIGHT"
		elif key == "q":
			self.event_type = "QUIT"
		else:
			self.event_type = ""


class Car:
	max_steering_angle = 450
	min_steering_angle = -450
	min_speed = -20
	max_speed = 200

	def __init__(self):
		self.wheel_angle = 0
		self.speed = 0


	def act (self, event):
		event_type = event.event_type

		if event_type == "SPEED UP":
			self.change_speed(10)
		elif event_type == "SLOW DOWN":
			self.change_speed(-5)
		elif event_type == "TURN LEFT":
			self.turn_steering_wheel(-10)
		elif event_type == "TURN RIGHT":
			self.turn_steering_wheel(10)
	
	def change_speed(self, value):
		new_speed = self.speed + value

		if self.is_max_speed_reached(value):
			self.speed = self.max_speed
		elif self.is_min_speed_reached(value):
			self.speed = self.min_speed
		else:
			self.speed += value

	def turn_steering_wheel(self, value):
		if self.is_max_angle_reached(value):
			self.wheel_angle = self.max_steering_angle
		elif self.is_min_angle_reached(value):
			self.wheel_angle = self.min_steering_angle
		else:
			self.wheel_angle += value

	def is_max_speed_reached(self, value):
		return self.speed + value > self.max_speed

	def is_min_speed_reached(self, value):
		return self.speed + value < self.min_speed

	def is_max_angle_reached(self, value):
		return self.wheel_angle + value > self.max_steering_angle

	def is_min_angle_reached(self, value):
		return self.wheel_angle + value < self.min_steering_angle

	def print_states(self):
		print("[speed: {}km/h, wheel angle: {}]".format(self.speed, self.wheel_angle))

car1 = Car()
event = Event()

print("Possible actions:")
print("press 'w' - increase speed by 10")
print("press 's' - decrease speed by 5")
print("press 'a' - turn steering wheel left by 10")
print("press 'd' - turn steering wheel right by 10\n")
print("To quit this app press 'q'...\n")

def main():
	while event.event_type != "QUIT":
		keyboard_input = input()

		event.detect_event_by_key_press(keyboard_input)
		car1.act(event)
		car1.print_states()

main()