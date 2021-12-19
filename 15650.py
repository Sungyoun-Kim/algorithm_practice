import sys


def dfs():
    if len(arr) == M:
        x=sorted(arr[:])
        if x in result:
            return
        result.append(x)
        return
    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    arr= []
    result= []
    dfs()
    for i in result:
        print(' '.join(map(str, i)))




