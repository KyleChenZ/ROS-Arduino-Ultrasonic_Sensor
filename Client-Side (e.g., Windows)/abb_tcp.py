#!/usr/bin/env python
import sys
from socket import socket,AF_INET,SOCK_STREAM, gethostbyname
import abb
TCP_IP = '192.168.1.73' #type your server ip
TCP_PORT = 10049 #if error occur, you can simply fix by changing this port number
SIZE = 1024  #predefined size for recv function
message = "1"
clientSocket =socket(AF_INET, SOCK_STREAM)#initial for a client socket
clientSocket.connect((TCP_IP, TCP_PORT))#wait for accept
movementA = 1;
a = 0;
try:
    print ("connecting to 192.168.125.1")
    r = abb.Robot(ip = '192.168.125.1')
except:
    a=1;
    print ("trying another ip address")
if(a==1):
    print ("connecting to 127.0.0.1")
    r=abb.Robot(ip='127.0.0.1')
r.set_speed([50,150,150,150])
while(True):
    clientSocket.send(message)#send the message
    receivedMessage = clientSocket.recv(SIZE)#receive message from server
    num = int(receivedMessage)
    print ("Received a message from client: "+receivedMessage)
    if num == '1':
        r.set_speed([50,150,150,150])
    elif num == '2':
        r.set_speed([100,150,150,150])
    elif num == '0':
        r.set_speed([400,150,150,150])
        #print ("Exit, returning to start position")
        #r.set_joints([0,0,0,0,0,0])
        #break
    movementA = movementA * -1
    if movementA == -1:
        r.set_cartesian([[800,0,1000],[0,0,1,0]])
    elif movementA == 1:
        r.set_cartesian([[600,0,1000],[0,0,1,0]])
    #this print message is not required by the assignment but just to indicate that the client has already send to message
print "\nExiting"
newSocket.close()
serverSocket.close()
sys.exit()
