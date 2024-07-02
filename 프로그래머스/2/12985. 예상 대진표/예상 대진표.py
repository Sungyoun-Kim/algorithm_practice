def solution(n,a,b):
    stage = 1
    while True:
        print(a,b)
        a= get_round(a)
        b= get_round(b)
        if a==b:
            return stage
        else:
            stage +=1
        
def get_round(num):
    if num%2 !=0:
        num = num+1
    if num == 0:
        num = 2
    
    return num //2
