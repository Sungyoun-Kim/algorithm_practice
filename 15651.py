import sys
def dfs():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1,N+1):

        result.append(i)
        dfs()
        result.pop()



if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    result = []
    dfs()

