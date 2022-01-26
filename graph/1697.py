import sys
from collections import deque


def bfs(n):
    queue = deque()
    queue.append(n)
    if n == K:
        return 0
    while queue:
        n = queue.popleft()
        if n+1 < len(arr) and arr[n+1] == 0:
            arr[n+1] = arr[n] + 1
            queue.append(n+1)
        if n-1 >= 0 and arr[n-1] == 0:
            arr[n-1] = arr[n] + 1
            queue.append(n-1)
        if n*2 < len(arr) and arr[n*2] == 0:
            arr[n*2] = arr[n] + 1
            queue.append(n*2)
    return arr[K]


if __name__ == "__main__":
    N, K = map(int,sys.stdin.readline().split())
    if K > N:
        arr = [0 for _ in range(100001)]
    else:
        arr = [0 for _ in range(100001)]

    print(bfs(N))


"""
숨바꼭질 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	135273	38287	23919	25.013%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.

출처
Olympiad > USA Computing Olympiad > 2006-2007 Season > USACO US Open 2007 Contest > Silver 2번

문제를 번역한 사람: author6
데이터를 추가한 사람: cohan, djm03178
비슷한 문제
12851번. 숨바꼭질 2
13549번. 숨바꼭질 3
13913번. 숨바꼭질 4
알고리즘 분류
그래프 이론
그래프 탐색
너비 우선 탐색
메모"""



