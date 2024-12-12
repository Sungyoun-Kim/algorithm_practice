import sys


def solution():
    N = int(sys.stdin.readline())

    balloons = list(map(int,sys.stdin.readline().split()))
    result = []
    result_len = 0
    boom = 9999
    idx = 0
    move = 0
    while True:
        if move==0 and balloons[idx] !=boom:
            result.append(idx+1)
            result_len+=1
            if result_len == N:
                print(' '.join(str(x) for x in result))
                return
            
            move = balloons[idx]
            balloons[idx] = boom
            continue
        
        elif move <0:
            idx -=1
            if idx <0:
                idx = N-1
            if balloons[idx] != boom:
                move +=1
        elif move >0:
            idx = (idx+1)%N
            if balloons[idx] != boom:
                move-=1
            
solution()

//생각해보니까 파이썬이라 음수 인덱스로 접근 되는데;;
