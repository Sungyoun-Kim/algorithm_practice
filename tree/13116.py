import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())

        while True:
            if A > B:
                A = A//2
            elif A < B:
                B = B//2
            elif A == B:
                print(10*A)
                break





