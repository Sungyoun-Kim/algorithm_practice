def solution(n, words):
    turn_count =1
    word_set = set()
    start_char = words[0][0]
    for i in range(len(words)):
        num = (i + 1) % n
        
        if words[i] in word_set or words[i][0] !=start_char:
            if num ==0:
                num =n
            return [num,turn_count]
        else:
            word_set.add(words[i])
            start_char = words[i][-1]
            if num == 0:
                turn_count+=1
    return [0,0]
    
        
            
