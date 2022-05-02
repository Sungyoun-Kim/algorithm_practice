import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    target = list(map(int, sys.stdin.readline().split()))
    A.sort()
    result = [0 for _ in range(M)]

    for i in range(M):
        start = 0
        end = len(A) - 1

        while end - start >= 0:
            mid = (start + end) // 2

            if A[mid] == target[i]:

                result[i] = 1
                break
            elif A[mid] < target[i]:
                start = mid + 1
                continue
            elif A[mid] > target[i]:
                end = mid-1
                continue

    for i in range(M):
        print(result[i], end=' ')


