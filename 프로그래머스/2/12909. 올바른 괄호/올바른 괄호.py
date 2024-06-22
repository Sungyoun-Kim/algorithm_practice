def solution(s):
    arr =[]
    s= list(s)
    s_len = len(s)
    while s_len > 0:
        s_len -=1
        bracket = s.pop()
        if bracket == ")":
            arr.append(bracket)
        else:
            if not arr:
                return False
            arr.pop()
            
    if not arr:    
        return True
    
    return False