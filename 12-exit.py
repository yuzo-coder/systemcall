import ctypes

libc = ctypes.CDLL(None)

libc.syscall(60, 0)
