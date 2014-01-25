#!/usr/bin/env python

"""
A simple echo server
"""

import socket

host = ''
port = 19290
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
print("listening for connections on port 19290")
while 1:
  client, address = s.accept()
  data = client.recv(size)
  if data:
    client.send(data)
  client.close()

