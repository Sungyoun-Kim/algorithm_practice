import sys

if __name__ =="__main__":
    expression = list(sys.stdin.readline().rstrip())
    razors =[]
    sticks = []
    stack = []

    idx = 0
    while idx < len(expression):
        if expression[idx] == '(' and expression[idx + 1] == ')':
            razors.append((idx, idx + 1))
            idx += 2
            continue
        if expression[idx] == '(':
            stack.append(idx)
            idx += 1
            continue
        if expression[idx] == ')':
            sticks.append((stack.pop(), idx))
            idx += 1
            continue
    answer = len(sticks)
    for start,end in sticks:
        for razor in razors:
            if start <= razor[0] <= end:
                answer+=1
    print(answer)






