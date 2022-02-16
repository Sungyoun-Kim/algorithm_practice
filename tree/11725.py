"""import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(arr[0])

    while queue:
        x, y = queue.popleft()
        for j in arr:
            if x in j:
                queue.append(j)
                arr.remove(j)

            elif y in j:
                queue.append(j)
                arr.remove(j)
        if result[x] == 0:
            result[x] = y
        elif result[y] == 0:
            result[y] = x

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = []
    result = [0 for _ in range(N+1)]
    result[1]= 1
    for i in range(N-1):
        X, Y = map(int, sys.stdin.readline().split())
        arr.append((X, Y))
    arr.sort()
    bfs()
    for i in result[2:]:
        print(i)
"""
import sys
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        print(queue)
        node = queue.popleft()
        print(node)

        for n in graph[node]:
            if p[n] == 0:
                p[n] = node
                queue.append(n)
        print(p)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
p = [0]*(N+1)
print(graph)
bfs(1)
for i in range(2, N+1):
    print(p[i])






