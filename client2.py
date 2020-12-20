import socket
import os
import subprocess
import sys
from _thread import *

clientsoc=socket.socket()

userip=input("Telnet: ")
host=userip
port=8080

clientsoc.connect((host,port))
comm=input("Enter The Command: ")

if comm == 'echo':
	print(comm[5:])

clientsoc.send(str.encode(comm))

while True:
	if comm == "quit":
		clientsoc.close()
		sys.exit()

	if comm != "quit":
		serv=clientsoc.recv(2048)
		print(serv.decode())
		comm=input("Enter The Command: ")

		bytesend=str.encode(comm)
		clientsoc.sendto(bytesend, (host,port))

	if comm == "echo":
		print(comm[5:])

clientsoc.close()
