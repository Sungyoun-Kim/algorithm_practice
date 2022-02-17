import sys

from collections import deque


def dfs(node):
    global count
    count += 1

    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
    return


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        N, M = map(int, sys.stdin.readline().split())
        minimum = 100001
        graph = [[] for _ in range(N + 1)]
        for j in range(M):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)
        visited = [0 for _ in range(N + 1)]
        count = 0
        dfs(1)
        minimum = min(minimum, count)
        print(minimum - 2)


