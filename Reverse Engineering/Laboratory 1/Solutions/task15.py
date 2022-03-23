#!/usr/bin/python3

from pwn import *
from itertools import permutations
from tqdm import tqdm

# These are the strings found at step 4
SPECIAL_STRINGS = []
SPECIAL_STRINGS.append("zihldazjcn")
SPECIAL_STRINGS.append("vlrgmhasbw")
SPECIAL_STRINGS.append("jqvanafylz")
SPECIAL_STRINGS.append("hhqtjylumf")
SPECIAL_STRINGS.append("yemlopqosj")
SPECIAL_STRINGS.append("mdcdyamgec")
SPECIAL_STRINGS.append("nhnewfhetk")

# This threshold is used to filter the "garbage" outputs
# Any possible flag, that doesn't have at least THRESHOLD printable ASCII characters, will be ignored
THRESHOLD = 20

# Generate all permutations of the "special" strings
perm = permutations(SPECIAL_STRINGS)

'''
Solution: nhnewfhetkmdcdyamgeczihldazjcnhhqtjylumfvlrgmhasbwjqvanafylzyemlopqosj
Flag: timctf{7dfadd1ee67a9c516c9efbf8f0cf43f4}
'''

# Input each possible permutation to the script
# tqdm only helps to display the progress
for idx, tuple_input in tqdm(enumerate(perm), ncols=100):

	current_input = ''.join(tuple_input)

	# start process using pwntools
	# no need to wrap it in ltrace this time
	p = process("./crackme", shell = True)

	# send as input the current iteration
	p.sendline(current_input)

	# wait for the program to end
	p.wait_for_close()
	
	# initialize a counter which helps us skip the first 2 lines
	# only the third is of interes, because it may contain the correct flag
	counter = 0
	# keep reading output until program terminates
	while True:
		try:
			#use "readline" from pwntools	
			line = p.readline()
			counter += 1

			# if this is the case, then we reach the line with the possible flag
			if counter == 3:
				# Count the "good" characters and print only the pairs (input, flag) with values above THRESHOLD
				good_characters = 0
				for char in line:
					good_characters += (32 <= char < 128)
				if good_characters > THRESHOLD:
					with open("output5.txt", "a") as fout:
						fout.write(current_input)
						fout.write("\n")
						for char in line: fout.write (chr(char))
						fout.write ("\n")
						fout.write ("\n")
		except:
			#could not read line => program exited
			break
