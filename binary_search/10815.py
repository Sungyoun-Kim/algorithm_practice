import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    base = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    target = list(map(int, sys.stdin.readline().split()))
    base.sort()

    for i in target:
        start = 0
        end = len(base)-1
        find = False
        while end >= start:
            mid = (start+end)//2

            if base[mid] == i:
                find = True
                break
            elif base[mid] < i:
                start = mid + 1
            elif base[mid] > i:
                end = mid - 1
        if find == True:
            print(1, end=' ')
        else:
            print(0, end=' ')





