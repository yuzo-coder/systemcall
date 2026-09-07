#!/usr/bin/env python3
import os
import fcntl

fd = os.open("./readme.txt", os.O_RDONLY)

fcntl.ioctl(fd, 0x5401)

os.close(fd)
