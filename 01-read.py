#!/usr/bin/env python3

import os

fd = os.open("./readme.txt", os.O_RDONLY)

data = os.read(fd, 100)

print(data.decode())

os.close(fd)
