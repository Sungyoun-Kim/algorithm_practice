import sys

if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    L = 0
    R = 0
    while True:
        if A < B:
            B = B - A
            R += 1
        elif A > B:
            A = A - B
            L += 1
        else:
            print(L,R)
            break
