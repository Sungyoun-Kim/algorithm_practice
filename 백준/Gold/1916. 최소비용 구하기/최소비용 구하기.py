import sys
import heapq

def dijkstra(start):
    queue = []
    distances[start] = 0

    heapq.heappush(queue,[0,start])

    while queue:
        c, x = heapq.heappop(queue)
        
        if distances[x] < c:
            continue
        for next, nextCost in graph[x]:
            distance = c + nextCost
            if distance < distances[next]:
                distances[next]=distance
                heapq.heappush(queue,[distance,next])


if __name__ =="__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    distances  = [int(10e9) for _ in range(N+1)]

    graph = [[]for _ in range(N+1)]
    for _ in range(M):
        startNode, endNode, cost = map(int,sys.stdin.readline().split())
        graph[startNode].append((endNode,cost))

    start, arrive = map(int,sys.stdin.readline().split())
    dijkstra(start)
    print(distances[arrive])
