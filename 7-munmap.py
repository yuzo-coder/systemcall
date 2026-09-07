import mmap

m = mmap.mmap(-1, 4096)

m[0:4] = b"AAAA"

m.close()
