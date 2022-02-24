import copy
import sys
from collections import deque
sys.setrecursionlimit(15000)

def bfs(a,b,cnt):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    while queue:
        a, b = queue.popleft()
        copied_Matrix[a][b] = cnt
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if copied_Matrix[nx][ny] != -1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,sys.stdin.readline().split())))
    biggest = max(map(max,matrix))
    safe_max = -1e9

    for i in range(biggest):
        copied_Matrix = copy.deepcopy(matrix)
        cnt = 0
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for j in range(N):
            for k in range(N):
                if copied_Matrix[j][k] <= i:
                    copied_Matrix[j][k] = -1
        for j in range(N):
            for k in range(N):
                if copied_Matrix[j][k] != -1 and visited[j][k] == 0:
                    cnt += 1
                    bfs(j, k,cnt)
        copied_max = max(map(max,copied_Matrix))
        safe_max = max(safe_max,copied_max)
    print(safe_max)


