import sys
from collections import deque

"""def dfs(x,y):
    way.append((x,y))
    global result
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if nx == N-1 and ny == M-1:
            result.append(len(way))

        if (nx,ny) not in way and matrix[nx][ny] == 1:
            dfs(nx, ny)
    way.pop()
    return
"""
def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y]+1
                queue.append((nx, ny))





if __name__ == "__main__":
    result = []
    way = []
    count = 0
    dx =[0, 0, -1, 1]
    dy =[1, -1, 0, 0]
    N, M = map(int,sys.stdin.readline().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,sys.stdin.readline().strip())))

    bfs(0,0)
    print(matrix[N-1][M-1])
"""

미로 탐색
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	192 MB	109513	45281	28991	39.956%
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15
예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9
예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38
예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13
출처
데이터를 추가한 사람: djm03178, jh05013, poia0304
알고리즘 분류
보기
"""