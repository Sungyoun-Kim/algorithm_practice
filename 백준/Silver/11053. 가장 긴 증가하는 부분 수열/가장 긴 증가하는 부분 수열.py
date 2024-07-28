import sys

def solution():
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    dp = [[1,A[i]] for i in range(N)]


    for i in range(0,N):
        for j in range(i,N):
            if dp[i][1] < dp[j][1]:
                dp[j][0] = max(dp[i][0]+1,dp[j][0])
    answer = 0
    for i in dp:
        answer = max(answer,i[0])
    print(answer)

solution()
