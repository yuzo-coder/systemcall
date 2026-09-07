import os

pid = os.fork()

if pid == 0:
    os._exit(0)

os.wait4(pid, 0)
print("child finished")
