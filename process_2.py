import socket
import sys
import time
import numpy
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #afinet for ipv4
s.connect((socket.gethostname(),1235))

def process_2():
    msg = s.recv(1024).decode("utf-8")
    print(msg+"\n")
    r1 = int(s.recv(1024).decode("utf-8"))
    print("recieved row1\n")
    c1 = int(s.recv(1024).decode("utf-8"))
    print("recieved col1\n")
    r2 = int(s.recv(1024).decode("utf-8"))
    print("recieved row2\n")
    c2 = int(s.recv(1024).decode("utf-8"))
    print("recieved col2\n")
    X = []
    Y = []
    R = []
    for i in range(r1*c1):
            x = int(s.recv(1024).decode("utf-8"))
            X.append(x)
    print("Received matrix 1\n")
    X = numpy.reshape(X,(r1,c1))
    for i in range(r2*c2):
            y = int(s.recv(1024).decode("utf-8"))
            Y.append(y)
    print("Received matrix 2\n")
    Y = numpy.reshape(Y,(r2,c2))
    print("Finding their product\n")
    R = numpy.dot(X,Y)
    print(R)
    print("sending resultant matrix to process 1\n")
    for i in range(r1):
        for j in range(c2):
            s.send(bytes(str(R[i][j]),"utf-8"))
            time.sleep(2)

process_2()
