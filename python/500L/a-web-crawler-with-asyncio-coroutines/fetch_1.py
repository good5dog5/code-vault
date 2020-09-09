#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess
import requests
import socket, ssl

def fetch_requests():
    resp = requests.get('https://xkcd.com')
    print(resp.text)

    # Page is now downloaded.
    # links = parse_links(response)
    # q.add(links)

def fetch_sock():
    HOST = 'xkcd.com'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, 443))
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
    s.sendall("GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".format(host=HOST).encode())
    response = b''
    chunk = s.recv(4096)
    while chunk:
        response += chunk
        chunk = s.recv(4096)

    print(response)

def fetch_1():

    HOST = "www.youtube.com"
    PORT = 443
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_sock = context.wrap_socket(s, server_hostname=HOST)
    s_sock.connect((HOST, 443))
    s_sock.sendall(" GET / HTTP/1.1\r\nHost: www.youtube.com\r\n\r\n ".encode())
    
    while True:
        data = s_sock.recv(2048)
        if ( len(data) < 1 ) :
            break
        print(data)
    
    s_sock.close()


if __name__ == '__main__':
    fetch_sock()

