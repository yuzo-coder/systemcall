import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 12345))

s.sendmsg([b"Hello"])

s.close()
