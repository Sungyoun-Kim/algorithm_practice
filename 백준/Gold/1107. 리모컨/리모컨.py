import sys

input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))


gap = abs(100 - target)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):

        if int(i[j]) in broken:
            break


        elif j == len(i) - 1:
            gap = min(gap, abs(int(i) - target) + len(i))

print(gap)