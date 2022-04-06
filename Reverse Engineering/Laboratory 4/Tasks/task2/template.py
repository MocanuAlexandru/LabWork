from pwn import *

context.arch = "amd64"
a = ELF.from_bytes( read("memorydump.bin") )
a.save("memorydump.elf")
