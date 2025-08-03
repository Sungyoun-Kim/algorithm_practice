import sys


T = int(sys.stdin.readline())
def getLength(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())

    if x1 ==x2 and y1 == y2 and r1 ==r2:
        print(-1)
        continue

    between =getLength(x1,y1,x2,y2)


    if r1+r2 == between or abs(r1-r2) == between:
        print(1)
        continue
    if between > r1+r2 or between < abs(r1-r2):
        print(0)
        continue
    if between < r1+r2 :
        print(2)
        continue
