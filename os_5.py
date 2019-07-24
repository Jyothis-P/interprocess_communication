from multiprocessing import Process, Queue
import os
import time
import numpy as np


def multiply(q, row, m, rn):
    r = []
    for i in range(len(m[0])):
        col = np.array(m)[:,i]
        s = 0
        for j in range(len(col)):
            s += row[j] * col[j]
        r.append(s)
    q.put([os.getpid(), rn, r])

if __name__ == '__main__':
    start_time = time.time()
    q = Queue()
    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
    # 3x4 matrix
    Y = [[5,8,1,2],
        [6,7,3,0],
        [4,5,9,1]]
    # result is 3x4
    result = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

    # iterate through rows of X
    for i in range(len(X)):
        p = Process(target=multiply, args=(q, X[i], Y, i))
        p.start()


    p.join()
    r = q.get()
    result[r[1]] = r[2]
    while q.qsize() > 0:
        r = q.get()
        result[r[1]] = r[2]
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
