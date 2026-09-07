import mmap
import os

fd = os.open("./readme.txt", os.O_RDONLY)

m = mmap.mmap(fd, 1000, mmap.MAP_PRIVATE, mmap.PROT_READ)

print(m[:10])

m.close()
os.close(fd)
