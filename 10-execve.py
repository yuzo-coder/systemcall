
import os

os.execve("/bin/echo", ["echo", "Hello"], {})
