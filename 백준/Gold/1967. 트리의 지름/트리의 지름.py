import sys
sys.setrecursionlimit(10**6)

def dfs(node,acc):
    for child,distance in tree[node]:
        if visited[child] !=0:
            continue
        visited[child] = acc+distance
    
        dfs(child,acc+distance)



if __name__ =="__main__":
    n = int(sys.stdin.readline())
    tree = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    r = 0
    for _ in range(n-1):
        parent, child, distance = map(int,sys.stdin.readline().split())
        tree[parent].append((child,distance))
        tree[child].append((parent,distance))

    visited[1] = -1
    dfs(1,0)
    r1 = max(visited)
    r1Index = visited.index(r1)
    visited = [0 for _ in range(n + 1)]
    visited[r1Index]= -1
    dfs(r1Index,0)
    print(max(visited))

    # r1 = max(visited)
    # r1Index = visited.index(r1)
    # visited[visited.index(r1)]=0
    # r2=max(visited)
    # r2Index = visited.index(r2)
    #
    # anscestorNode = 1
    # i=0
    # while True:
    #     if path[r1Index][i] != path[r2Index][i]:
    #         anscestorNode = path[r1Index][i-1]
    #         break
    #     i+=1
    # print(r1+r2-visited[anscestorNode]*2)







