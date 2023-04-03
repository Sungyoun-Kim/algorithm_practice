import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    P = list(map(int,sys.stdin.readline().split()))
    P.insert(0,0)
    dp = [0 for _ in range(N+1)]
    dp[1]=P[1]
    dp[2]=max(2*P[1],P[2])
    for i in range(2,N+1):
        for j in range(i+1):
            dp[i]= max(dp[i],dp[j]+dp[i-j],P[i])
    print(dp[-1])










