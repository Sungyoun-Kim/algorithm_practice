"""import sys


def solution(sec):
    global xcount
    global ycount
    global zcount
    if 0 < sec < 10:
        print(-1)
        return

    if sec // x >= 1:
        xcount+=1

        return solution(sec - x)
    if sec // y >=1:
        ycount+=1
        return solution(sec - y)
    if sec // z >= 1:
        zcount+=1
        return solution(sec - z)
    if sec == 0:
        print(xcount,ycount,zcount)
        return

if __name__ == "__main__":
    S = int(sys.stdin.readline())
    x = 300
    xcount = 0
    y = 60
    ycount = 0
    z = 10
    zcount = 0
    solution(S)
""" # 위에는 재귀로 해봄
import sys

if __name__ == "__main__":
    S = int(sys.stdin.readline())
    if S%10:
        print(-1)
    else:
        A=B=C=0
        A = S//300
        B = (S%300)//60
        C = ((S%300)%60)//10
        print(A,B,C)