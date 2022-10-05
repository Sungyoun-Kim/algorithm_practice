import copy


def solution(triangle):
    dp = copy.deepcopy(triangle)
    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            for k in range(j, j + 2):
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + triangle[i + 1][k])

    return max(dp[-1])




