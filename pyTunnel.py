#!/usr/bin/python
import socket
import sys
from thread import *

#Functions
#Auth Function
#def authenticator(data)

#handler
def handler(conn1, conn2):
    #Send message on connect
    conn1.send("200")
    conn2.send("200")

    while True:
        #Receive from socket 1
        data = conn1.recv(1024)
        #Send to socket 2
        conn2.sendall(data)
    #Close if loop ends
    conn1.close()
    conn2.close()

if __name__ == "__main__":
    #Define listener and ports
    HOST = '' #all interfaces
    PORT1 = 5335 #client 1
    PORT2 = 5334 #client 2

    #Create Sockets
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Sockets made"

    #Bind sockets
    try:
        s1.bind((HOST, PORT1))
        s2.bind((HOST, PORT2))
    except socket.error as msg:
        print "Bind failed: " + str(msg[0]) + "Message " + msg[1]
        sys.exit()
    print "Socket binding complete"

    #Start Listening 
    s1.listen()
    s2.listen()
    print "Sockets now listening"

    #authenticator()
    #if auth passes continue...
    while 1:
        #wait to accept a connection
        conn1 = s1.accept()
        conn2 = s2.accept()
        #start thread
        start_new_thread(handler, (conn1, conn2)) 
s1.close()
s2.close()
