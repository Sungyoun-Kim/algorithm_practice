import sys
from itertools import permutations

if __name__ == "__main__":

    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    op = list(map(int, sys.stdin.readline().split()))
    OP = ["+", "-", "*", "//"]
    comb = []
    MAX = -1000000000
    MIN = 1000000000
    while True:
        for i in range(4):
            if op[i] > 0:
                comb.append(i)
                op[i] = op[i] - 1
        if op[0] + op[1] + op[2] + op[3] == 0:
            break

    for i in permutations(comb, N - 1):
        exp = ""
        x = list(i)
        for j in range(N - 1):
            exp = "(" + exp + str(num[j]) +")"+ str(OP[x[j]])
        exp = exp + str(num[-1])
        print(exp,eval(exp))
        MAX = max(eval(exp),MAX)
        MIN = min(eval(exp),MIN)
    print(MAX)
    print(MIN)
