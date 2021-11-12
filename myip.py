import socket
import urllib
import sys
def myip(ip):
    print("ip address is",(socket.gethostbyname(ip)))
myip(sys.argv[1])