import sys

def solution():
    N= int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    B=  list(map(int,sys.stdin.readline().split()))
    M =int(sys.stdin.readline())
    C =list(map(int,sys.stdin.readline().split()))


    p = [B[i] for i in range(N) if A[i] == 0]
    p.reverse()
    p = p[:M]
    
    for i in C:
        if len(p) >= M:
            break
        p.append(i)
    
    print(' '.join(map(str,p)))



solution()