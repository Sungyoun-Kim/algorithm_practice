def solution(arr):
    for i in range(1,len(arr)):
        arr[i]= arr[i] * arr[i-1] //gcd(arr[i],arr[i-1])
    return arr[-1]

        
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

        
    
    