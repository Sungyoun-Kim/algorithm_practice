import sys

def robotAction(y,x,direction):
    global cleaned

    if matrix[y][x]==0:
        cleaned+=1
        matrix[y][x]=2

    isBlocked = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= M or nx < 0 or ny >=N or ny <0 or matrix[ny][nx] != 0:

            isBlocked += 1



    if isBlocked != 4:
        if matrix[y+dy[(direction+3)%4]][x+dx[(direction+3)%4]] == 0:
            robotAction(y+dy[(direction+3)%4], x+dx[(direction+3)%4], (direction+3)%4)
            return
        else:
            robotAction(y, x,  (direction+3)%4)
            return
    else:
        kx =x+dx[(direction+2)%4]
        ky = y+dy[(direction+2)%4]
        if matrix[ky][kx] == 1:
            print(cleaned)
            return

        robotAction(ky,kx,direction)
        return

if __name__=="__main__":
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    N, M = map(int,sys.stdin.readline().split())
    robot=list(map(int,sys.stdin.readline().split()))
    matrix = []
    global cleaned
    cleaned=0

    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))


    robotAction(robot[0],robot[1],robot[2])

