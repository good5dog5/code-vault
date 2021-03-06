#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess


import socket, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('xkcd.com', 443))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
s.sendall("GET / HTTP/1.1\r\nHost: xkcd.com\r\nConnection: close\r\n\r\n".encode())

while True:

    new = s.recv(4096)
    if not new:
      s.close()
      break
    print (new)
