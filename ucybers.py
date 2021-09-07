#############
import os
import socket
#############
s = socket.socket()
port = 4444
host = input(str("Enter The Server To Start ==> "))
s.connect((host,port))
print ("")
print ("Good..! Connected To The Server Success.. ")
print ("")
#############
while 1:
    command = s.recv(1024)
    command = command.decode()
    print ("Done.. Command Recieved..!")
    print ("")
    if command == "ucybers":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print ("Done.. Command Executed..! ")
    elif command == "ls":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print ("Done.. Command Executed..! ")
#############
    else:
        print ("")
        print ("Ooh..! Command Err..!!")
#############
