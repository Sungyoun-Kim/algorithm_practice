import heapq
import sys

if __name__ =="__main__":
    N = int(sys.stdin.readline())
    timeTable = []
    room = []
    for _ in range(N):
        S, T = map(int, sys.stdin.readline().split())
        timeTable.append([S, T])

    timeTable.sort()
    heapq.heappush(room, timeTable[0][1])

    for i in range(1,N):
        if timeTable[i][0] < room[0]:
            heapq.heappush(room,timeTable[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room,timeTable[i][1])
    print(len(room))








