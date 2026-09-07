import ctypes

libc = ctypes.CDLL(None)

fd = libc.syscall(257, -100, b"./readme.txt", 0)

print(fd)

libc.close(fd)
