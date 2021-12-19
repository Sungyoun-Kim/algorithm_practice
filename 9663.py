import sys

def dfs(n):

    if n == N:
        global count
        count+=1
    else:
        for i in range(N):
            if visited[i]:
                continue
            chess[n] = i
            if check(n):
                visited[i] = True
                dfs(n+1)
                visited[i] = False

def check(n):
    for i in range(n):
        if chess[n] == chess[i]  or (n-i == abs(chess[n]-chess[i])):
            return False
    return True



if __name__ == "__main__":
    count=0
    N = int(sys.stdin.readline())
    visited = [False for _ in range(N)]
    chess = [0 for _ in range(N)]
    dfs(0)
    print(count)

