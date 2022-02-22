import sys
from itertools import combinations_with_replacement



if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    L = []
    for i in range(1,N+1):
        L.append(i)
    for i in combinations_with_replacement(L, M):
        for j in i:
            print(j,end=' ')
        print()




