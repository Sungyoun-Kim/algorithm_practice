import sys


def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, N+1):
        if arr[v][i] == 1 and visited[i] == 0:
            dfs(i)


def bfs(v):
    queue = [v]
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if arr[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1


if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(N+1)]

    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, M+1):
        A, B = map(int, sys.stdin.readline().split())
        arr[A][B] = 1
        arr[B][A] = 1

    dfs(V)
    print()
    visited = [0 for _ in range(N+1)]
    bfs(V)



