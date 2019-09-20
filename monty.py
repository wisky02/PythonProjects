# Code for experimentally validating the monty hall problem

from random import *
import numpy as np
class bcolours:
	WARNING = '\033[93m'
	ENDC = '\033[0m'
	UNDERLINE = '\033[92m'
def choosing_problem():
	while True:
		run_choice = raw_input("Manual(M) or simulated(S)?")
		if (run_choice == "M"):
			print("You have chosen manual opperation")
		elif (run_choice == "S"):
			print("You have chosen simluated opperation")
		else:
			print bcolours.WARNING +  "ERROR: Please choose a valid character: (M) or (S)" +bcolours.ENDC
			continue
		return run_choice

def simulation(num_loops):
	counter = 0
	win_change_counter = 0
	win_stick_counter = 0
	for x in range(num_loops):
		boxes = [1,2,3]
		winning_box = sample(boxes, 1)
		box_choice = sample(boxes, 1)
		# stick loop
		if (box_choice == winning_box):
			win_stick_counter = win_stick_counter + 1
		# change loop
		boxes_rand = boxes[:]
		boxes_rand.remove(winning_box[0])
		if box_choice[0] in boxes_rand:
			boxes_rand.remove(box_choice[0])
		rand_choice = sample(boxes_rand, 1)
		boxes_change = boxes[:]
		boxes_change.remove(rand_choice[0])
		boxes_change.remove(box_choice[0])
		box_change_choice = boxes_change[0]
		if (box_change_choice == winning_box[0]):
			win_change_counter = win_change_counter + 1
		else:
			continue
		counter = counter + 1
	print "win by stick: ", win_stick_counter
	print  "win by change: ", win_change_counter
	return

def manual(): 
	keep_playing = True
	counter = 0
	win_counter = 0
	win_change_counter = 0
	win_stick_counter = 0
	while(keep_playing):
		doors = [1,2,3]	
		print "-----------   -----------   -----------"
		for x in range(2):
        		print "|         |   |         |   |         |"
		print "|    1    |   |    2    |   |    3    |"
		for x in range(2):
        		print "|         |   |         |   |         |"
		print "-----------   -----------   -----------"	
		while(True):
			door_choice_input = raw_input("Choose a door: ")
			if (door_choice_input.isdigit()):
				if(int(door_choice_input) in doors):
					break
				else:
					print bcolours.WARNING + "Choose one of the doors!" + bcolours.ENDC
			else:
				print bcolours.WARNING + "Please enter a positive integer" +bcolours.ENDC
		door_choice = int(door_choice_input)
		winning_door = sample(doors, 1)
		remove_doors = doors[:]
		remove_doors.remove(winning_door[0])
		if (door_choice in remove_doors):
			remove_doors.remove(door_choice)
		remove_door = sample(remove_doors, 1)
		if remove_door[0] == 1:
			print "-----------   -----------   -----------"
			for x in range(2):
        			print "|xxxxxxxxx|   |         |   |         |"
			print "|xxxx1xxxx|   |    2    |   |    3    |"
			for x in range(2):
        			print "|xxxxxxxxx|   |         |   |         |"
			print "-----------   -----------   -----------"
		elif remove_door[0] == 2:
			print "-----------   -----------   -----------"
			for x in range(2):
        			print "|         |   |xxxxxxxxx|   |         |"
			print "|    1    |   |xxxx2xxxx|   |    3    |"
			for x in range(2):
        			print "|         |   |xxxxxxxxx|   |         |"
			print "-----------   -----------   -----------"
		elif remove_door[0] == 3:
			print "-----------   -----------   -----------"
			for x in range(2):
        			print "|         |   |         |   |xxxxxxxxx|"
			print "|    1    |   |    2    |   |xxxx3xxxx|"
			for x in range(2):
        			print "|         |   |         |   |xxxxxxxxx|"
			print "-----------   -----------   -----------"
		else:
			print bcolours.WARNING + "Error in door removal" +bcolours.ENDC
		valid_doors = doors[:]
		valid_doors.remove(remove_door[0])
		switch_door = valid_doors[:]
		switch_door.remove(door_choice)
		while(True):
			new_choice_input = raw_input("Do you want to stick " + "(" + str(door_choice)+")" + " with your original choice, door " +str(door_choice) + " or switch " +"(" + str(switch_door[0]) +")" + " to door " + str(switch_door[0]) + "? ")
			if (new_choice_input.isdigit()):
				if(int(new_choice_input) in valid_doors):
					break
				else:
					print bcolours.WARNING + "Please make a valid integer choice between changing or sticking." + bcolours.ENDC
			else:	
				print bcolours.WARNING + "Please make a valid integer choice between changing or sticking" + bcolours.ENDC
		new_choice = int(new_choice_input)
		if (new_choice == winning_door[0]):
			print bcolours.UNDERLINE + "YOU WIN!" + bcolours.ENDC
			win_counter = win_counter + 1
			if (new_choice == door_choice):
				win_stick_counter = win_stick_counter + 1
			else:
				win_change_counter = win_change_counter + 1
		else:
			print bcolours.UNDERLINE + "You lose this time!" + bcolours.ENDC
	
		counter = counter + 1
		while(True):
			keep_playing_input = raw_input("Play another round? (yes/no)")
			if(keep_playing_input == "yes" or keep_playing_input == "no"):
				if(keep_playing_input == "no"):
					keep_playing = False
					break
				elif(keep_playing_input == "yes"):
					break
			else:
				print bcolours.WARNING + "please choose \"yes\" or \"no\"" + bcolours.ENDC

	print bcolours.UNDERLINE +  "YOUR RESULTS" + bcolours.ENDC
	print "Total number of rounds: " , counter		
	print "Total number of wins:  " , win_counter
	print "Total number of wins by changing: ", win_change_counter
	print "Total number of wins by sticking: ", win_stick_counter
	return



run_choice = choosing_problem()

if(run_choice == "M"):
	print("Welcome to the game show!")
	manual()

elif(run_choice == "S"):
	print("Welcome robo-contestants!")
	while(True):
		num_loops_input = raw_input("Please enter the number of contests - the higher the number the better the accuray:")
		if (num_loops_input.isdigit()):
			break
		else:
			print bcolours.WARNING + "Please enter a positive integer" +bcolours.ENDC
	num_loops = int(num_loops_input)
	simulation(num_loops)
