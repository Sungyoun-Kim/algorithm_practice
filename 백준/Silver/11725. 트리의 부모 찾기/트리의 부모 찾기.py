import sys
sys.setrecursionlimit(10**6)

def dfs(node,parent):
    answer[node]=parent
    for i in tree[node]:
        if visited[i]==0:
            visited[i]=1
            dfs(i,node)







if __name__ =="__main__":
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    answer = [0 for _ in range(N+1)]


    for i in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    visited[1]=1
    dfs(1,0)
    for i in answer[2:]:
        print(i)


