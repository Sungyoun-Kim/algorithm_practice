import sys
sys.setrecursionlimit(1000000)

def query(node):
    global count
    visited[node]=1


    for i in tree[node]:
        if not visited[i]:
            query(i)
            visited[node] += visited[i]



if __name__ == "__main__":
    N, R, Q = map(int,sys.stdin.readline().split())
    tree = [[]for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]


    for i in range(N-1):
        U, V = map(int,sys.stdin.readline().split())
        tree[U].append(V)
        tree[V].append(U)

    query(R)
    for i in range(Q):
        q = int(sys.stdin.readline())
        print(visited[q])






