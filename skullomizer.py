from random import randint
import random
import linecache

used_skulls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
current_skulls = [0,0,0,0,0]
number_changes = [0,0,0,0,0]
amt_skulls = 0
bonus_amt = 0

def gen_skull( ):
	x = 0
	while x == 0: 
		skull_no = randint(0, 99)
		if used_skulls[skull_no] == 0:
			x = 1
	return skull_no

# Set seed
seed = raw_input('Seed: ')
random.seed(seed)

flash = raw_input('Flash mode? (y/n):')

bonus = raw_input('Bonus points for all 5 finished? (y/n):')
if bonus == "y":
	bonus_amt = int(raw_input("How many points for a bonus?:"))

for skull in range (0,5):
	# Choose 5 random numbers between 0 and 99
	skull_no = gen_skull()

	# Set them as used
	used_skulls[skull_no] = 1

	# And set the current skulls to those 5
	current_skulls[skull] = skull_no
for skull in range (0,5):

	# Print current skulls
	#textline = linecache.getline("skulls.txt", current_skulls[skull])
	textline = linecache.getline("skulls.txt", current_skulls[skull] + 1)
	print("[ ]"+str(skull + 1) + ". "+textline)

while 1:
	# Get input for which completed skull
	number = raw_input('Skull no.:')
	number_int = int(number) - 1
	# Increment points
	amt_skulls += 1

	# Check for bonuses
	number_changes[number_int] = 1
	num_bonuses = 0
	for skull in range (0,5):
		if number_changes[skull] == 1:
			num_bonuses += 1
	if (num_bonuses == 5) & (bonus_amt > 0):
		amt_skulls += bonus_amt
		print(str(bonus_amt) + " point bonus!")
		for skull in range (0,5):
			number_changes[skull] = 0

	# Print amount of points
	print("Points: " + str(amt_skulls))
	
	if flash == "y":
		for skull in range(0,5):
			skull_no = gen_skull()
			used_skulls[current_skulls[number_int]] = 1
			current_skulls[skull] = skull_no
	else:
		skull_no = gen_skull()
		used_skulls[skull_no] = 1
		current_skulls[number_int] = gen_skull()

	# Set it as used and add it to the current 5 to replace the last gotten skull
	
	current_skulls[number_int] = skull_no

	# Print current skulls
	for skull in range (0,5):
		textline = linecache.getline("skulls.txt", current_skulls[skull] + 1)
		checkbox = " "
		if number_changes[skull] == 1:
			checkbox = "X"
		print("[" + checkbox + "]" +  str(skull+1) + ". "+textline)


