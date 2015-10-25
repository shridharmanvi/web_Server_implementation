import socket
import urlparse
import re
import os

socket.setdefaulttimeout = 0.50
os.environ['no_proxy'] = '127.0.0.1,localhost'
linkRegex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
CRLF = "\r\n\r\n"


def GET(url):
    url = urlparse.urlparse(url)
    path = url.path
    if path == "":
        path = "/"
    HOST = url.netloc  # The remote host
    PORT = 80          # The same port as used by the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.30)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #s.setblocking(0)
    s.connect((HOST, PORT))
    s.send("GET / HTTP/1.0%s" % (CRLF))
    data = (s.recv(1000000))

    print data
    # https://docs.python.org/2/howto/sockets.html#disconnecting
    s.shutdown(1)
    s.close()
    print 'Received', repr(data)