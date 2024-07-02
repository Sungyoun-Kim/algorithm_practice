def solution(k, tangerine):
    t_dict = {}
    for t in tangerine:
        if not t in t_dict:
            t_dict[t] = 1
        else:
            t_dict[t] +=1
    t= sorted(t_dict.items(), key = lambda item: item[1], reverse = True)
    answer = 0
    t_count = 0
    for key_value in t:
        t_count += key_value[1]
        answer+=1
        if t_count >=k:
            return answer


    
    