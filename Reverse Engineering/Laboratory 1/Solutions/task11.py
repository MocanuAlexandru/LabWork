#!/usr/bin/python3

from pwn import *

# start process using pwntools
p = process("./crackme")

# send an input (e.g. 1234)
p.sendline("1234")

# keep reading output until program terminates
while True:
	try:
		line = p.readline()
		#use "readline" from pwntools
		print ("Read line: [%s]" % line)
	except:
		#could not read line => program exited
		break


