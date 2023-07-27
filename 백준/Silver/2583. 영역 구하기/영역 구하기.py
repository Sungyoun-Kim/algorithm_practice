import sys
import collections
# def dfs(x,y):
#     global M
#     global N
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#         matrix[ny][nx] = 1
#         dfs(nx,ny)
#
def bfs(x,y):
    global M
    global N
    queue = collections.deque()
    queue.append((x,y))

    area = 0

    while queue:
        xx,yy = queue.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[ny][nx] ==0:
                queue.append((nx,ny))
                matrix[ny][nx] =1
                area+=1

    if area ==0:
        return 1
    return area




if __name__ == "__main__":
    M, N, K = map(int,sys.stdin.readline().split())
    dx =[0,1,0,-1]
    dy = [1,0,-1,0]

    matrix = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(K):
        ax, ay, bx, by = map(int,sys.stdin.readline().split())

        for j in range(by-ay):
            for k in range(bx - ax):
                matrix[M-1-ay-j][ax+k] =1
    area = []
    count = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                count+=1
                area.append(bfs(j,i))

    print(count)
    area.sort()
    print(*area)



