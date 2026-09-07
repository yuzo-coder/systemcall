import socket

s = socket.socket()

s.bind(("127.0.0.1", 12346))
s.listen()

c, addr = s.accept()

c.close()
s.close()
