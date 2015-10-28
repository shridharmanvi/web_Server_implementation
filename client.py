import socket
import urlparse
import sys
import re
import os

host = '127.0.0.1'
port = 8011
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
CRLF = "\r\n\r\n"

def GET(url):
    #print url
    url = urlparse.urlparse(url)
    path = url.path
    get_statement = 'GET ' + str(path) + 'HTTP/1.0'
    print get_statement
    #s.send("GET / HTTP/1.0%s" % (CRLF))
    s.send("GET " + get_statement)
    data = (s.recv(1000000))
    s.shutdown(1)
    s.close()
    print 'Received', repr(data)



def GET1(url):
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
    #print 'Received', repr(data_received)
    print data_received


def POST(body):
    #host = '127.0.0.1'
    #port = 8011
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((host, port))

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
    if sys.argv[1] == 'POST':
        POST('userName=shridhar.manvi&password=manvishridhar')
    else:
        if sys.argv[1] == 'GET':
            GET1('http://127.0.0.1:8010/www/ima')

