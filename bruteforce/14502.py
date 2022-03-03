import copy
import sys
from collections import deque


def bfs():

    count_zero = 0
    queue = deque()
    copied_matrix = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(M):
            if copied_matrix[i][j] == 2:
                queue.append((i, j))
    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if copied_matrix[nx][ny] == 0:
                copied_matrix[nx][ny] = 2
                queue.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if copied_matrix[i][j] == 0:
                count_zero += 1

    return count_zero


def wall(cnt):
    global max_safe
    if cnt == 3:
        max_safe = max(bfs(), max_safe)

        return
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                wall(cnt+1)
                matrix[i][j] = 0


if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    matrix = []
    max_safe = -1e9
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    wall(0)
    print(max_safe)
