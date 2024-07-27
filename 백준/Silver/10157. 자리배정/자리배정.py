import sys

def solution():
    C, R = map(int,sys.stdin.readline().split())
    # R은 y 축의 길이, C는 x축의 길이
    K = int(sys.stdin.readline())
    seats = [[0 for _ in range(C)] for _ in range(R)]
    x = 0
    y = R-1
    #시작은 R-1, 0부터이다
    if K > C*R:
        print(0)
        return
    if C*R ==1:
        print(1)
        return 
    seats[y][x]= 1
    direction = "UP"
    k = 2
    while k <=K+1:
        if k == K+1:
            print(x+1,R-y)
            return
            
        if direction =="UP":
            if y- 1 >= 0 and seats[y -1][x] == 0:
                y= y-1
                seats[y][x] = k
                k+=1
                
            else:
                direction = "RIGHT"
            continue
        elif  direction == "RIGHT":
            if x+1 <= C-1 and seats[y][x+1] == 0:
                x= x+1
                seats[y][x] = k
                k+=1
            else:
                direction = "DOWN"
            continue
        elif  direction =="DOWN":
            if y+1<= R-1 and seats[y +1][x] == 0:
                y= y+1
                seats[y][x] = k
                k+=1
            else:
                direction = "LEFT"
            continue
        elif direction == "LEFT":
            if x -1 >= 0 and seats[y][x-1] == 0:
                x=x-1
                seats[y][x] = k
                k+=1
            else:
                direction = "UP"
            
    
solution()
