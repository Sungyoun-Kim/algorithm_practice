import sys

def getDistance(startNode,targetNode):
    visited[startNode]=1

    global distance
    for i in tree[startNode]:
        if visited[i[0]]:
            continue
        if i[0]==targetNode:
            print(distance+i[1])

        distance+=i[1]
        getDistance(i[0],targetNode)
        distance-=i[1]






if __name__ =="__main__":
    N, M =map(int,sys.stdin.readline().split())
    tree = [[] for _ in range(N+1)]


    for _ in range(N-1):
        U, V, D = map(int, sys.stdin.readline().split())
        tree[U].append((V,D))
        tree[V].append((U,D))

    for _ in range(M):
        distance = 0
        visited = [0 for _ in range(N+1)]
        start,target = map(int,sys.stdin.readline().split())
        getDistance(start,target)



