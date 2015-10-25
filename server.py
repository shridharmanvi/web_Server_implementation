__author__ = 'shridharmanvi'

import socket


host = ''
port = 8011
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)  # don't queue up any requests

while True:
    print 'Server running.....'
    csock, caddr = sock.accept()  # Accepts connection
    print "Connection from: " + str(caddr)
    message = csock.recv(1024)  # get the request, 1kB max
    print 'Message: ', message
    request = message.split() # Main request received from the client
    request_method = str(request[0])
    filename = str(request[1])

    try:
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        csock.send('HTTP/1.0 200 OK\r\n\r\n')
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            csock.send(outputdata[i])
        csock.close()
    except:
        if filename == '/':
            csock.send('HTTP/1.0 200 OK\r\n\r\n')
            f = open('home.html')
            send_data = f.read()
            for i in range(0, len(send_data )):
                csock.send(send_data[i])
            csock.close()
        else:
            csock.send('HTTP/1.1 404 Not Found\r\n\r\n')
            f = open('file_not_found.html')
            send_data = f.read()
            for i in range(0, len(send_data )):
                csock.send(send_data [i])
            csock.close()

    csock.close()