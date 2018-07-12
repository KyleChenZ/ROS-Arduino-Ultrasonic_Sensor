#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import sys
from socket import socket,AF_INET,SOCK_STREAM, gethostbyname
TCP_IP = '192.168.1.73' #type your server ip
try:
	TCP_PORT = 10049 #if error occur, you can simply fix by changing this port number
except:
	TCP_PORT = TCP_PORT - 1
	print(TCP_PORT)
SIZE = 1024  #predefined size for recv function
hostName = gethostbyname( '0.0.0.0' )
serverSocket = socket(AF_INET, SOCK_STREAM) #initial for a server socket
serverSocket.bind((hostName, TCP_PORT)) #binding to 0.0.0.0 means to bind to every IP address on this machine
serverSocket.listen(5) #listening for client request
newSocket, addr = serverSocket.accept() #accept a request from its client

def callback(data):
	
	rospy.loginfo(rospy.get_caller_id() + "\nmessage: %f",data.data)

	receivedMessage = newSocket.recv(SIZE)
	if data.data <= 50 and data.data >= 0:
		newSocket.send('1')
	elif data.data <= 100 and data.data > 50:
		newSocket.send('2')
	elif data.data == -1:
		newSocket.send('-1')
	else:
		newSocket.send('0')
	
def listener():
	rospy.init_node('sonar_listen',anonymous=True)
	rospy.Subscriber("sonar",Float32,callback)
	rospy.spin()

if __name__ == '__main__':
	listener()

print "\nExiting"
newSocket.close()
serverSocket.close()
sys.exit()
