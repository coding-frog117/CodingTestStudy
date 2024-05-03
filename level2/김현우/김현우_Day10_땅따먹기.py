from copy import deepcopy


def solution(land):
    # 2차원 DP 탐색
    dp = deepcopy(land)

    for i in range(1, len(dp)):
        for j in range(4):
            temp = 0
            # i행 j열 최대값을 찾을 때, i-1행의 j열을 제외한 다른 값들 중 최대값을 찾아 더함
            for k in range(4):
                if j == k:
                    continue
                temp = max(temp, dp[i - 1][k])
            dp[i][j] += temp

    return max(dp[-1])