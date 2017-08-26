from random import randint
import random
import linecache

# Set seed
seed = raw_input('Seed: ')
random.seed(seed)

used_skulls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
current_skulls = [0,0,0,0,0]
amt_skulls = 0

for skull in range (0,5):
	# Choose 5 random numbers between 0 and 99
	skull_no = randint(0, 99)
	# Set them as used
	used_skulls[skull_no] = 1
	# And set the current skulls to those 5
	current_skulls[skull] = skull_no
for skull in range (0,5):
	# Print current skulls
	textline = linecache.getline("skulls.txt", current_skulls[skull])
	print(str(skull + 1) + ". "+textline)

while 1:
	# Get input for which completed skull
	number = raw_input('Skull no.:')
	number_int = int(number) - 1
	# Increment and display points
	amt_skulls += 1
	print("Points: " + str(amt_skulls))
	# Generate random numbers until a valid uncompleted skull is found
	x = 0
	while x == 0: 
		skull_no = randint(0, 99)
		if used_skulls[skull_no] == 0:
			x = 1
	# Set it as used and add it to the current 5 to replace the last gotten skull
	used_skulls[skull_no] = 1
	current_skulls[number_int] = skull_no
	# Print current skulls
	for skull in range (0,5):
		textline = linecache.getline("skulls.txt", current_skulls[skull])
		print(str(skull+1) + ". "+textline)