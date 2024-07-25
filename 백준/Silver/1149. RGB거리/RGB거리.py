import sys

N = int(sys.stdin.readline())
houses = [0 for _ in range(N)]
for i in range(N):
    houses[i]=list(map(int,sys.stdin.readline().split()))
dp = [[10e9,10e9,10e9] for _ in range(N)]
dp[0] = houses[0]

for i in range(1,N):
    for j in range(3):
        for k in range(1,3):
            idx = (j+k) % 3 
            dp[i][j]= min(dp[i][j],dp[i-1][idx] + houses[i][j])

print(min(dp[-1]))