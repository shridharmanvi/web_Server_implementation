__author__ = 'shridharmanvi'

import socket


host = ''
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)  # don't queue up any requests

while True:
    print 'Server running.....'
    csock, caddr = sock.accept()  # Accepts connection
    print "Connection from: " + `caddr`