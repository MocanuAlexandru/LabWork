#!/usr/bin/python3

from pwn import *

# start process using pwntools
# wrap the process in ltrace this time
p = process("ltrace ./crackme", shell = True)

# send input
p.sendline("1234")

# Initialize an array for library function calls
fct_calls = []
# keep reading output until program terminates
while True:
	try:
		#use "readline" from pwntools
		line = p.readline()
		#if the line doesn't start with '-' or '+', register a library function call
		if line[0] != 45 and line[0] != 43:
			line = line.decode('utf-8')
			ind_par = line.find("(")
			if ind_par != -1:
				# append to the array what can be found until '('
				line = line[:ind_par]
				fct_calls.append(line)
	except:
		#could not read line => program exited
		break

print(fct_calls)
