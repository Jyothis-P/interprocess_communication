import socket
import sys
import time
import numpy
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1235))
s.listen(5)

def process_1():
    clientsocket,address = s.accept()
    time.sleep(2)
    print("Connection established.\n")
    clientsocket.send(bytes("Connection established.","utf-8"))
    time.sleep(2)
    print("Enter the first matrix size")
    r1 = int(input())
    c1 = int(input())
    print("enter elements\n")
    X = []
    for i in range(r1*c1):
        x = int(input())
        X.append(x)
    X = numpy.reshape(X,(r1,c1))
    print(X)
    print("Enter the second matrix size\n")
    r2 = int(input())
    c2 = int(input())
    Y = []
    print("enter elements\n")
    for i in range(r2*c2):
        y = int(input())
        Y.append(y)
    Y = numpy.reshape(Y,(r2,c2))
    print(Y)
    print("senting matrix sizes\n")
    clientsocket.send(bytes(str(r1),"utf-8"))
    time.sleep(1)
    clientsocket.send(bytes(str(c1),"utf-8"))
    time.sleep(1)
    clientsocket.send(bytes(str(r2),"utf-8"))
    time.sleep(1)
    clientsocket.send(bytes(str(c2),"utf-8"))
    time.sleep(1)
    R = []
    print("elements of matrix 1 being sent to process 2 for multiplication\n")
    for i in range(r1):
        for j in range(c1):
            clientsocket.send(bytes(str(X[i][j]),"utf-8"))
            time.sleep(1)
    print("elements of matrix 2 being sent to process 2 for multiplication\n")
    for i in range(r2):
        for j in range(c2):
            clientsocket.send(bytes(str(Y[i][j]),"utf-8"))
            time.sleep(1)
        '''r = int(clientsocket.recv(1024).decode("utf-8"))
        print("received result\n\nappending result to final result\n")
        R.append(r)'''
    print("Receiving resultant matrix\n")
    for i in range(r1*c2):
        r = int(clientsocket.recv(1024).decode("utf-8"))
        print(r)
        R.append(r)
    print("Received resultant matrix\n")
    R = numpy.reshape(R,(r1,c2))
    time.sleep(1)
    print("printing resultant matrix\n")
    print(R)

process_1()
