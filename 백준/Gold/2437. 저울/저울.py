import sys

def solution():
    N = int(sys.stdin.readline())
    weights = list(map(int,sys.stdin.readline().split()))
    weights.sort()
    
    answer =1
    for i in weights:
        if answer < i:
            break
        answer += i
    print(answer)

    
    
    
        
solution()