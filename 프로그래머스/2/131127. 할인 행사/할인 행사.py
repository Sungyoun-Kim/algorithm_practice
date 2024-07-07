def solution(want, number, discount):
    needs_dict = dict(zip(want,number))
    
    day = 0
    answer = 0
    while day+10 <= len(discount):
        nd = needs_dict.copy()
        for i in range(day,day+10):
            d = discount[i]
            if d in nd:
                nd[d] -=1 
            else:
                continue
                
        is_satisfied = True
        for _,value in nd.items():
            if value >0:
                is_satisfied =False
                break
        if is_satisfied:
            answer+=1
        day +=1
        
    return answer