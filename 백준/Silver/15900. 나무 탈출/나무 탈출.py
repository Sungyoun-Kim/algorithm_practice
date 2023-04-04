import sys
sys.setrecursionlimit(100000)



def dfs(node,path):
    global totalPath

    isVisited[node]=1
    for i in tree[node]:
     
        if isVisited[i] != 0:
            continue
        dfs(i,path+1)


    if len(tree[node])==1:
        totalPath=totalPath+path
    return


if __name__ =="__main__":
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    isVisited = [0 for _ in range(N+1)]
    totalPath = 0
    for _ in range(N-1):
        x, y = map(int,sys.stdin.readline().split())
        tree[x].append(y)
        tree[y].append(x)

    dfs(1,0)


    if totalPath % 2 == 0:
        print('No')
    else:
        print('Yes')








