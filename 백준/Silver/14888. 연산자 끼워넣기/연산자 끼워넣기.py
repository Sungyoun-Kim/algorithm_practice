import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
# +,-,*,/
op = list(map(int,sys.stdin.readline().split()))
opArr = []
for i in range(op[0]):
    opArr.append('+')
for i in range(op[1]):
    opArr.append('-')
for i in range(op[2]):
    opArr.append('*')
for i in range(op[3]):
    opArr.append('/')

min_result = float('inf')
max_result = float('-inf')

def calc(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if a <0:
            a= abs(a)
            result = a //b 
            return -result
        else:
            return a//b


visited = [False for _ in range(len(opArr))]
selectedOp =[]

def backtracking(idx):
    global min_result
    global max_result

    if idx == N-1:
        result = A[0]
        for i in range(N-1):
            result = calc(result,A[i+1],selectedOp[i])
        min_result = min(min_result,result)
        max_result = max(max_result,result)
        return 
    for i in range(len(opArr)):
        if not visited[i]:
            visited[i] = True
            selectedOp.append(opArr[i])   
            backtracking(idx+1)
            visited[i] = False
            selectedOp.pop()

backtracking(0)
print(max_result)
print(min_result)
