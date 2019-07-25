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
    for i in range(r1):
        sum_ = 0
        for j in range(c2):
            x = int(s.recv(1024).decode("utf-8"))
            y = int(s.recv(1024).decode("utf-8"))
            print("received elements\n")
            sum_ = sum_ + x + y
        print("sending result to process 1 for elements received\n")
        s.send(bytes(str(sum_),"utf-8"))
        time.sleep(2)

process_2()
