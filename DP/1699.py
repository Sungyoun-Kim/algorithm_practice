import sys
import math
def DP(n):

    if n <4:
        print(n)
        return
    dp = [100 for _ in range(n+1)]
    dp[0]=0
    dp[1]=1
    dp[2]=2
    dp[3]=3
    for i in range(1,n+1):
        for j in range(0,int(math.sqrt(i))-1):
            dp[i] = min(dp[i - 1] + 1,dp[i-pow(int(math.sqrt(i))-j,2)]+1,dp[i])


    print(dp[N])


if __name__ =="__main__":
    N = int(sys.stdin.readline())
    DP(N)




""" 
 1699번
제출
맞힌 사람
숏코딩
재채점 결과
채점 현황
내 제출
강의
질문 검색
제곱수의 합
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	37549	15040	10919	39.216%
문제
어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데, 11의 경우 11=22+22+12+12+12(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

출력
주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

예제 입력 1 
7
예제 출력 1 
4
예제 입력 2 
1
예제 출력 2 
1
예제 입력 3 
4
예제 출력 3 
1
예제 입력 4 
11
예제 출력 4 
3
예제 입력 5 
13
예제 출력 5 
2
출처
ICPC > Regionals > Asia Pacific > Korea > Nationwide Internet Competition > Seoul Nationalwide Internet Competition 2007 E번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: godmoon00
데이터를 추가한 사람: sbukkk, yukariko
알고리즘 분류
수학
다이나믹 프로그래밍"""