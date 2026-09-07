import ctypes
import os

fd = os.open("./readme.txt", os.O_RDONLY)

ctypes.CDLL(None).syscall(3, fd)
