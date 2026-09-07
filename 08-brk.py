import ctypes

libc = ctypes.CDLL(None)

libc.syscall(12, 0)
