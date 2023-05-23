def solution(lottos, win_nums):
    answer =[]
    count =0
    zero_count =0
    for lotto in lottos:
        if lotto ==0:
            zero_count+=1
            
    for lotto in lottos:
        for num in win_nums:
            if lotto == num:
                count+=1
    
    if count >1:
        answer.append(7-count)
        answer.append(7-(count+zero_count))
    else:
        answer.append(6)
        if count+zero_count > 1:
            answer.append(7-(count+zero_count))
        else:
            answer.append(6)
    
    
    
    
            
        
    return sorted(answer)