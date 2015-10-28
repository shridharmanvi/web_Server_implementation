import socket
import urlparse
import sys
import re
import os

host = str(sys.argv[1])
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
CRLF = "\r\n\r\n"

log = open('client_log', 'a')



def GET(url):
    url = urlparse.urlparse(url)
    path = url.path

    headers = "GET " + path + """ HTTP/1.1\r
    Host: {host}\r
    Connection: close\r
    \r\n"""

    header_bytes = headers.format(
        content_type="application/x-www-form-urlencoded",
        host=str(host) + ":" + str(port)
    ).encode('iso-8859-1')
    send_data = header_bytes
    s.send(send_data)
    data_received = (s.recv(1000000))
    s.shutdown(1)
    s.close()
    log.writelines(data_received)
    log.writelines('\n --------------------- \n')
    #print 'Received', repr(data_received)
    print data_received


def POST(body):
    headers = """\
    POST /auth HTTP/1.1\r
    Content-Type: {content_type}\r
    Content-Length: {content_length}\r
    Host: {host}\r
    Connection: close\r
    \r\n"""

    body = body
    body_bytes = body.encode('ascii')
    header_bytes = headers.format(
        content_type="application/x-www-form-urlencoded",
        content_length=len(body_bytes),
        host=str(host) + ":" + str(port)
    ).encode('iso-8859-1')

    payload = header_bytes + body_bytes
    s.send(payload)


if __name__ == '__main__':
    if sys.argv[3] == 'POST':
        POST(sys.argv[4])
    else:
        if sys.argv[3] == 'GET':
            GET(sys.argv[4])



"""
python client.py 127.0.0.1 8011 GET 'http://127.0.0.1:8010/home.html'
"""

"""
python client.py 127.0.0.1 8011 POST 'username=shridharmanvi'
"""