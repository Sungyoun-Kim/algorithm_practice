def solution(n):
    answer = 0
    for i in range(1,n):
        acc = i 
        for j in range(i+1,n):
            acc = acc + j
            if acc <= n:
                if acc == n:
                    answer+=1
                    break
                continue
            break
            
    return answer+1
