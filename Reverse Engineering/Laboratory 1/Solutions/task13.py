#!/usr/bin/python3

from pwn import *

# try different lengths for the input (0 to 99 characters)
for i in range(100):
	# start process using pwntools
	# the process is wrapped as previously into ltrace
	p = process("ltrace ./crackme", shell = True)

	# send input of length i
	p.sendline("1" * i)

	# wait for the program to finish
	p.wait_for_close()
	
	# similar to exercise to we print to a file the function calls (for each length)
	with open("output3.txt", "a") as fout:
		fout.write(str(i) + " --> ")
		fct_calls = []
		while True:
			try:
				#use "readline" from pwntools
				line = p.readline()
				if line[0] != 45 and line[0] != 43:
					line = line.decode('utf-8')
					ind_par = line.find("(")
					if ind_par != -1:
						line = line[:ind_par]
						fct_calls.append(line)
			except:
				#could not read line => program exited
				break
		fout.write(str(fct_calls))
		fout.write("\n")

