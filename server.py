__author__ = 'shridharmanvi'

import socket
import thread

host = ''
port = 8011
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)  # don't queue up any requests



def server_func(csock, caddr):
    message = csock.recv(1024)  # get the request, 1kB max
    log = open('./server_log', 'a')
    log.writelines(str(message))
    log.writelines('\n ------------------ \n')
    log.close()
    #print 'Message: ', message
    request = message.split() # Main request received from the client
    #print request[-1]
    request_method = str(request[0])
    filename = str(request[1])

    if request_method == 'GET':
        try:
            f = open(filename[1:])
            outputdata = f.read()
            f.close()
            #Send one HTTP header line into socket
            http_resp = """HTTP/1.0 200 OK\r\n\r\n"""

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                http_resp =http_resp + outputdata[i]

            csock.send(http_resp)
            csock.close()
        except:
            if filename == '/':
                http_resp = """HTTP/1.0 200 OK\r\n\r\n"""
                #csock.send('HTTP/1.0 200 OK\r\n\r\n')
                f = open('home.html')
                send_data = f.readlines()
                for i in range(0, len(send_data)):
                    http_resp = http_resp + send_data[i]

                csock.send(http_resp)
                csock.close()
            else:
                http_resp = """HTTP/1.1 404 Not Found\r\n\r\n"""

                f = open('file_not_found.html')
                send_data = f.readlines()
                for i in range(0, len(send_data)):
                    http_resp = http_resp + send_data[i]

                csock.send(http_resp)
                csock.close()
    else:
        if request_method == 'POST':
            print message
            #print 'message sent by POST request: \n', request[-1]
            csock.close()

    csock.close()

if __name__ == '__main__':
    while True:
        print 'Server running.....\n'
        csocket, caddress = sock.accept()  # Accepts connection
        thread.start_new_thread(server_func, (csocket, caddress)) # Start thread for every new request


