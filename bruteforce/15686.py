import sys
from itertools import combinations

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    result = 0
    house = []
    chicken = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                house.append((i+1, j+1))
            elif matrix[i][j] == 2:
                chicken.append((i+1, j+1))

    mini = 1e7
    for i in range(1, M+1): # 몇 개 남길껀지
        for pmt in combinations(chicken, i): # 폐업 경우의수
            all_distance = 0
            for j in house:
                distance = 1e7
                for k in pmt:
                    distance = min(distance,abs(j[0]-k[0]) + abs(j[1] - k[1]))
                all_distance += distance
            mini = min(all_distance,mini)
    print(mini)










