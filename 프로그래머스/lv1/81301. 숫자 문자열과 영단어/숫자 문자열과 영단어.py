def solution(s):
    dict = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    
    answer =[]
    cache = ""
    for i in s:

         if i.isalpha():
            cache+=i
            
         else:
            answer.append(i)
         if len(cache) > 0:
            if cache in dict:
                answer.append(dict[cache])
                cache=""
 
            
            
        
            
 
    return int(''.join(answer))