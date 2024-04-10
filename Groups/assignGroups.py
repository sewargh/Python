import sys
import random

if len(sys.argv) > 1: #check if there is an argument in the terminal.
	numUsers=sys.argv[1] # take the argument from the terminal.

	list = [] #empty list to store the trainees numbers 
	list.extend(range(1,int(numUsers)+1)) #fill the list (sorted)
	random.shuffle(list) #shuffle the list to be random.
	print(list)
	

	num = int(numUsers) % 3 #check if the students are dividable by 3 or not.
	if num == 0: #the students number divides by 3 -- all the groups are with equal number of members.
		
		for i in range(0,int(numUsers),3): #iterating for every 3 trainees starting from index 0
			print(list[i:3+i]) #used slicing to print each group trainee members. starting from the index i to the next 3 indices.

	else:
		if num == 1: #"two members alone"
			for i in range(0,int(numUsers),3): #iterating for every 3 trainees 
				print(list[i:3+i])
			print(list[int(numUsers)-1]) #print the last group 2 members
		else: #one member alone
			for i in range(0,int(numUsers),3):
				print(list[i:3+i]) #used slicing to print each group trainee members.
			print(list[int(numUsers)-2:int(numUsers)-1]) #print the last group 1 member
else:
	print("no input. please re-run the script and enter the trainess numbers in the command line argument")
