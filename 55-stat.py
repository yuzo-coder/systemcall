import ctypes

libc = ctypes.CDLL(None)

buf = ctypes.create_string_buffer(512)

ret = libc.stat(b"./readme.txt", buf)

print(ret)
