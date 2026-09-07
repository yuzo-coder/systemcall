#!/usr/bin/env python3

import os

fd = os.open("./readme.txt", os.O_WRONLY)

os.write(fd, b"A" * 1000)

os.close(fd)
