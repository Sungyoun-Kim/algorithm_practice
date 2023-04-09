import sys
sys.setrecursionlimit(10**6)
def getPraise(praiseTarget):
    for i in tree[praiseTarget]:
        dp[i]+=dp[praiseTarget]
        getPraise(i)




if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    parents = list(map(int,sys.stdin.readline().rstrip().split()))
    tree = [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    for i in range(1,len(parents)):
        tree[parents[i]].append(i+1)

    for _ in range(m):
        i, w = map(int, sys.stdin.readline().split())
        dp[i]+=w

    getPraise(1)

    dp.pop(0)
    print(*dp)






