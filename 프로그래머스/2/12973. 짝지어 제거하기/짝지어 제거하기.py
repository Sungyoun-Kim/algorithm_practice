def solution(s):
    stack = [s[0]]
    for i in range(1,len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
            continue
        stack.append(s[i])
    if not stack:
        return 1
    else:
        return 0
        