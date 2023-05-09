def dfs(num,count):
    if count ==500:
        return -1
    if num ==1:
        return count
    if num %2 ==0:
        num = num/2
    else:
        num = num*3+1
    return dfs(num,count+1)
    

def solution(num):
    return dfs(num,0)
    