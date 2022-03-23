#!/usr/bin/python

from pwn import * # sudo pip install pwntools


# start process interaction
# use "process" from pwntools

# send input
# use "send"/"sendline" from pwntools

# keep reading output until program terminates
while True:
	try:
		#use "readline" from pwntools
		print "Read line: [%s]" % line

		#TODO 
	except:
		#could not read line => program exited
		break


