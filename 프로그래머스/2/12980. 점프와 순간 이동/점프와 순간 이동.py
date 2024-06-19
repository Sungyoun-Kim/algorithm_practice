

def solution(n):
    answer= 1
    while n%2!=n:
        if n % 2 !=0:
            n= n-1
            answer+=1
        else:
            n=n//2
    return answer
            
        
        
    # arr = [0,1,1]
    # for i in range(2,n+1):
    #     if i%2==0 or i%2==i:
    #         arr.append(arr[i//2])
    #     else:
    #         arr.append(arr[i-1]+1)
    # print(arr)
    # return arr[-1]