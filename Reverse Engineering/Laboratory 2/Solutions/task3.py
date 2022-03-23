from ctypes import c_uint64 as unsigned_int64

# the argument
rdi = int(input())

rdx = 0x43BC07457929CF79
rax = rdi
# mul rdx
rdx = (rax * rdx) >> 64
print("rdx: ", rdx)
# end mul rdx (skip rax change, it is not relevant because it will be overwrite)
rdi = unsigned_int64(rdi - rdx)
print("rdi - rdx: ", rdi)
rdi = unsigned_int64(rdi.value >> 1)
print("(rdi - rdx)/2: ", rdi)
rax = unsigned_int64(rdx + rdi.value)
rax = unsigned_int64(rax.value >> 11)
print("Result: ", rax)