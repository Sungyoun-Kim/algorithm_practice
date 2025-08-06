import sys
from collections import deque

c, l = map(int,sys.stdin.readline().split())

board = []
for i in range(c):
    board.append(list(sys.stdin.readline()[:-1]))





def bfs(i,j):
    ans = 0
    queue = deque()
    queue.append((i,j,0))
    visited= [[False]*l for _ in range(c)]
    visited[i][j]=True
    while queue:
        x,y,d= queue.popleft()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if nx < 0 or nx >= c or ny < 0 or ny >= l:
                continue
            if board[nx][ny] == "W":
                continue
            else:
                if visited[nx][ny] == False :
                    queue.append((nx,ny,d+1))
                    visited[nx][ny] = True
                    ans= d+1
    return ans

result =0  
for i in range(c):
    for j in range(l):
        if board[i][j] == "L":
            result = max(result,bfs(i,j))
print(result)


                


        