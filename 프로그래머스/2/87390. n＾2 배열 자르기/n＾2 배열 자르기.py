def solution(n, left, right):
#     arr = [[0 for _ in range(n)] for _ in range(n)]
    
#     for i in range(n):
#         for j in range(n):
#             arr[i][j] = max(i,j)+1
            
#     flatten_arr = []
#     for a in arr:
#         flatten_arr = flatten_arr + a
     
#     return flatten_arr[left:right+1]
# 시간초과 

# left,right 는 nx + y 는 라고 할 수 있음
    answer = []
    l = n*n
    for i in range(left,right+1):
        c =i//n 
        r = i%n 
        answer.append(max(r,c)+1)
    return answer
        
        