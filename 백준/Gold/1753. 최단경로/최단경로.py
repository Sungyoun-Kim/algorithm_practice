import heapq
import sys

def dijkstra(start):
    queue = []
    INF = sys.maxsize
    heapq.heappush(queue, (0,start))
    distance = [INF for _ in range(V+1)]
    distance[start] = 0
    while queue:
  
        weight,now = heapq.heappop(queue)
        if distance[now] < weight:
            continue
        for value,next_node in graph[now]:
            next_wei = weight+value
            if distance[next_node] > next_wei:
                distance[next_node] = next_wei
                heapq.heappush(queue,(next_wei,next_node))

    for i in range(1, V + 1):
        print("INF" if distance[i] == INF else distance[i])




if __name__=="__main__":
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v,w = map(int,sys.stdin.readline().split())
        graph[u].append((w,v))
    dijkstra(K)

