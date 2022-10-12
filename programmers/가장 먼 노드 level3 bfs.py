import sys

sys.setrecursionlimit(10000)
from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    dist = [0 for _ in range(n + 1)]

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    def bfs(node):
        distance = 1
        queue = deque()
        for i in node:
            queue.append([i, distance])
        while queue:
            node, distance = queue.popleft()
            if dist[node] == 0:
                dist[node] = distance
                for i in graph[node]:
                    queue.append([i, distance + 1])

    bfs(graph[1])
    dist = dist[2:]
    return dist.count(max(dist))

#     def dfs(node,distance):
#         for i in node:
#             if len(graph[i]) ==0:
#                 if dist[i] > distance:
#                     dist[i] = distance
#                 return
#             if dist[i] < distance:
#                 continue
#             else:
#                 dist[i]=distance
#             dfs(graph[i],distance+1)
#     dfs(graph[1],1)
#     dist = dist[2:]
#     return dist.count(max(dist))




