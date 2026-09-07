#!/usr/bin/env python3
import os
import ctypes

libc = ctypes.CDLL(None)

fd = os.open("./readme.txt", os.O_RDONLY)

r, w = os.pipe()

ret = libc.syscall(275, fd, 0, w, 0, 100, 0)

print("splice:", ret)

os.close(fd)
os.close(w)

data = os.read(r, 100)
print(data.decode())

os.close(r)
