import copy
import sys
from collections import deque

if __name__=="__main__":
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    field = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(K):
        y, x = map(int,sys.stdin.readline().split())
        field[y][x] = -1
    L = int(sys.stdin.readline())
    direction = [1,2,3,4] #북동남서
    dy= [-1,0,1,0]
    dx= [0,1,0,-1]
    snake = deque([(1,1)])
    head = 1 # direction index
    move = deque([0 for _ in range(10000)])
    for _ in range(L):
        sec,dir = sys.stdin.readline().split()

        move[int(sec)] = dir

    flag=False
    for i in range(0,10000):





        change = move.popleft()
        if change == 'L':
            head = (head - 1) % 4
        if change == 'D':
            head = (head + 1) % 4


        nx=0
        ny=0
        for j in range(4):
            if head == j:
                y, x = snake[0]
                ny =y + dy[j]
                nx= x + dx[j]

                if (ny, nx) in snake or ( ny >N or ny <=0 or nx >N or nx <=0 ):
                    flag = True
                    break
                snake.appendleft((ny,nx))


        if flag:
            print(i+1)
            break

        if field[ny][nx] !=-1:
            snake.pop()
        else:
            field[ny][nx]=0

# 뱀
# 성공다국어
#
# 시간
# 제한
# 메모리
# 제한
# 제출
# 정답
# 맞힌
# 사람
# 정답
# 비율
# 1
# 초
# 128
# MB
# 54652
# 22539
# 15035
# 39.486 %
# 문제
# 'Dummy'
# 라는
# 도스게임이
# 있다.이
# 게임에는
# 뱀이
# 나와서
# 기어다니는데, 사과를
# 먹으면
# 뱀
# 길이가
# 늘어난다.뱀이
# 이리저리
# 기어다니다가
# 벽
# 또는
# 자기자신의
# 몸과
# 부딪히면
# 게임이
# 끝난다.
#
# 게임은
# NxN
# 정사각
# 보드위에서
# 진행되고, 몇몇
# 칸에는
# 사과가
# 놓여져
# 있다.보드의
# 상하좌우
# 끝에
# 벽이
# 있다.게임이
# 시작할때
# 뱀은
# 맨위
# 맨좌측에
# 위치하고
# 뱀의
# 길이는
# 1
# 이다.뱀은
# 처음에
# 오른쪽을
# 향한다.
#
# 뱀은
# 매
# 초마다
# 이동을
# 하는데
# 다음과
# 같은
# 규칙을
# 따른다.
#
# 먼저
# 뱀은
# 몸길이를
# 늘려
# 머리를
# 다음칸에
# 위치시킨다.
# 만약
# 이동한
# 칸에
# 사과가
# 있다면, 그
# 칸에
# 있던
# 사과가
# 없어지고
# 꼬리는
# 움직이지
# 않는다.
# 만약
# 이동한
# 칸에
# 사과가
# 없다면, 몸길이를
# 줄여서
# 꼬리가
# 위치한
# 칸을
# 비워준다.즉, 몸길이는
# 변하지
# 않는다.
# 사과의
# 위치와
# 뱀의
# 이동경로가
# 주어질
# 때
# 이
# 게임이
# 몇
# 초에
# 끝나는지
# 계산하라.
#
# 입력
# 첫째
# 줄에
# 보드의
# 크기
# N이
# 주어진다.(2 ≤ N ≤ 100) 다음
# 줄에
# 사과의
# 개수
# K가
# 주어진다.(0 ≤ K ≤ 100)
#
# 다음
# K개의
# 줄에는
# 사과의
# 위치가
# 주어지는데, 첫
# 번째
# 정수는
# 행, 두
# 번째
# 정수는
# 열
# 위치를
# 의미한다.사과의
# 위치는
# 모두
# 다르며, 맨
# 위
# 맨
# 좌측(1
# 행
# 1
# 열) 에는
# 사과가
# 없다.
#
# 다음
# 줄에는
# 뱀의
# 방향
# 변환
# 횟수
# L
# 이
# 주어진다.(1 ≤ L ≤ 100)
#
# 다음
# L개의
# 줄에는
# 뱀의
# 방향
# 변환
# 정보가
# 주어지는데, 정수
# X와
# 문자
# C로
# 이루어져
# 있으며.게임
# 시작
# 시간으로부터
# X초가
# 끝난
# 뒤에
# 왼쪽(C가
# 'L') 또는
# 오른쪽(C가
# 'D')로
# 90
# 도
# 방향을
# 회전시킨다는
# 뜻이다.X는
# 10, 000
# 이하의
# 양의
# 정수이며, 방향
# 전환
# 정보는
# X가
# 증가하는
# 순으로
# 주어진다.
#
# 출력
# 첫째
# 줄에
# 게임이
# 몇
# 초에
# 끝나는지
# 출력한다.
#
# 예제
# 입력
# 1
# 6
# 3
# 3
# 4
# 2
# 5
# 5
# 3
# 3
# 3
# D
# 15
# L
# 17
# D
# 예제
# 출력
# 1
# 9
# 예제
# 입력
# 2
# 10
# 4
# 1
# 2
# 1
# 3
# 1
# 4
# 1
# 5
# 4
# 8
# D
# 10
# D
# 11
# D
# 13
# L
# 예제
# 출력
# 2
# 21
# 예제
# 입력
# 3
# 10
# 5
# 1
# 5
# 1
# 3
# 1
# 2
# 1
# 6
# 1
# 7
# 4
# 8
# D
# 10
# D
# 11
# D
# 13
# L
# 예제
# 출력
# 3
# 13
# 출처
# Olympiad > Croatian
# Highschool
# Competitions in Informatics > 2005 > National
# Competition  # 1 - Juniors 2번
#
# 문제의
# 오타를
# 찾은
# 사람: dlwocks31, hax3
# 빠진
# 조건을
# 찾은
# 사람: doju, joonas, zhsks311
# 문제를
# 번역한
# 사람: sehun
# 알고리즘
# 분류
# 구현
# 자료
# 구조
# 시뮬레이션
# 덱
# 큐
#
#
#
#
#
#
#

