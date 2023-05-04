import sys
import heapq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    queue =[]
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x != 0:
            heapq.heappush(queue,(abs(x),x))
        else:
            try:
                print(heapq.heappop(queue)[1])
            except:
                print(0)



