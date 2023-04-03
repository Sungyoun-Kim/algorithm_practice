import sys
from collections import deque

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        P = sys.stdin.readline().rstrip()
        N = int(sys.stdin.readline())
        X = sys.stdin.readline()

        x = deque(eval(X))

        isReversed = False
        isError = False
        for i in P:
            if i == 'R' and isReversed == False:
                isReversed = True
            elif i=='R' and isReversed == True:
                isReversed=False

            if i == 'D' and isReversed == True:
                if(len(x)==0):
                    isError=True
                    break
                x.pop()
            elif i== 'D' and isReversed == False:
                if (len(x) == 0):
                    isError = True
                    break
                x.popleft()

        if(isError):
            print('error')
        elif isReversed:
            x.reverse()
            print(str(list(x)).replace(' ',''))
        else:
            print(str(list(x)).replace(' ',''))
