import sys

N = int(sys.stdin.readline())
visited = [False] * (N + 1)
arr = []

def permutation():
    if len(arr) == N:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            permutation()
            arr.pop()
            visited[i] = False


permutation()