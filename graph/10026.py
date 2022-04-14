import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        X, Y = queue.popleft()
        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 0 and matrix[X][Y] == matrix[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1


if __name__ =="__main__":
    matrix = []
    N = int(sys.stdin.readline())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0
    for i in range(N):
        matrix.append(list(sys.stdin.readline().strip()))

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt += 1
                bfs(i,j)
    print(cnt)
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'G':
                matrix[i][j] = 'R'

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt += 1
                bfs(i,j)
    print(cnt)


"""
적록색약 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	31769	18365	14308	57.335%
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1 
4 3
출처
Olympiad > USA Computing Olympiad > 2013-2014 Season > USACO March 2014 Contest > Bronze 3번

문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: corea
알고리즘 분류
그래프 이론
그래프 탐색
너비 우선 탐색
깊이 우선 탐색
메모"""

