from collections import deque

def solution(s):
    bracket_dict = {
        "}":"{",
        "]":"[",
        ")":"(",
    }
    
    answer=0
    for i in range(len(s)):
        
        stack = []
        new_s = s[i:] + s[:i]
        for j in range(len(s)):
            b = new_s[j]
            if b in  bracket_dict:
                if stack and stack[-1] == bracket_dict[b]:
                    stack.pop()
                    continue
            stack.append(b)
        
        if not stack:
            answer +=1
    return answer