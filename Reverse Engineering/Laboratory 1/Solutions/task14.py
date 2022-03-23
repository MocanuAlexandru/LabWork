#!/usr/bin/python3

from pwn import *

# The length found at task 3
LENGTH = 70
# The special strings that we are finding during this step
# I added each string after I found it
SPECIAL_STRING = ""
SPECIAL_STRING += "zihldazjcn"
SPECIAL_STRING += "vlrgmhasbw"
SPECIAL_STRING += "jqvanafylz"
SPECIAL_STRING += "hhqtjylumf"
SPECIAL_STRING += "yemlopqosj"
SPECIAL_STRING += "mdcdyamgec"
SPECIAL_STRING += "nhnewfhetk"
# At each step the remaining length decreases (as we insert newly found "special" strings in the input)
REMAINING_LENGTH = 0

# start process using pwntools
# the process is wrapped inside ltrace, as in the previous tasks
p = process("ltrace ./crackme", shell = True)


# the input contains the "special" string found so far
# in the end we append as many '1' as neccessary to reach the correct length
p.sendline(SPECIAL_STRING + "1" * (REMAINING_LENGTH))

# keep reading output until program terminates
while True:
	try:
		#use "readline" from pwntools
		line = p.readline()
		# print the output from ltrace to a file
		# used this to find the next "special" string at each step
		with open("output4.txt", "a") as fout:
			fout.write ("Read line: [%s]" % line)
			fout.write ("\n")
		
	except:
		#could not read line => program exited
		break


