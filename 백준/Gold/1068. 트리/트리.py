import sys



def dfs(children):

    global count

    for i in children:
        if len(children)==1 and i==deleteNode:
            count+=1
            continue
            
        if i == deleteNode:
            continue
            
        if len(tree[i]) == 0 and visited[i] == 0:
            count += 1
            visited[i] = 1
            continue
            
        if visited[i] == 1:
            continue

        dfs(tree[i])


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    parents = list(map(int,sys.stdin.readline().split()))
    tree =[[]for _ in range(N)]
    visited = [0 for _ in range(N)]
    deleteNode = int(sys.stdin.readline())
    count =0

    root = -999
    for i in range(len(parents)):
        if parents[i] ==-1:
            root = i
            continue
        tree[parents[i]].append(i)

    if deleteNode!=root:
        visited[root]=1
        dfs(tree[root])
        print(count)
    else:
        print(0)




