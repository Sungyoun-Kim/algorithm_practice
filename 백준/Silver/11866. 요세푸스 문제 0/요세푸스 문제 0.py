import sys
import time
def sol():
    N,K=map(int,sys.stdin.readline().split())
    d = [False for _ in range(N)]
    result = []

    idx= 0
    move= 0
    while len(result) <N:
        if idx == N:
            idx = idx % N

        if move ==K-1 and d[idx] ==False:
            result.append(idx+1)
            d[idx] = True
            move = 0
            continue

        if d[idx] == True:
            idx +=1
            continue
        move+=1
        idx+=1

    print("<"+str(result)[1:-1]+">")

    


sol()