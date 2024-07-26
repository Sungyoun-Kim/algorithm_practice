
# Online Python - IDE, Editor, Compiler, Interpreter
import sys

N,m= map(int,sys.stdin.readline().split())

required_boxes = []
for i in range(m):
    required_boxes.append(int(sys.stdin.readline()))
required_boxes.sort()

answer =0
for i in required_boxes:
    N-=i
    if N < 0:
        break
    answer+=1
print(answer)
    
