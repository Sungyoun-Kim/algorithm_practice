import sys
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] =1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] =1

                distance[i] = distance[now]+1
                if distance[i]==K:
                    answer.append(i)
                queue.append(i)



if __name__ == "__main__":
    N, M, K, X = map(int, sys.stdin.readline().split())
    answer = []
    graph = [[] for _ in range(N + 1)]
    distance = [0 for _ in range(N + 1)]
    visited = [0 for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int,sys.stdin.readline().split())
        graph[A].append(B)
    bfs(X)

    doesExist = False
    for i in range(len(distance)):
        if distance[i]==K:
            doesExist=True
            print(i)
    if not doesExist:
        print(-1)




