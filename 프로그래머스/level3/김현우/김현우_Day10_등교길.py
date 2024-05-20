def solution(m, n, puddles):
    # DP 2차원 배열 하나 만들어서 위에서 아래로, 왼쪽에서 오른쪽으로 탐색
    dp = [[0 for _ in range(m)] for __ in range(n)]

    # dp 배열에 puddles 위치 표시
    for p in puddles:
        dp[p[1] - 1][p[0] - 1] = -1

    # 1행, 1열 전처리
    if dp[0][0] == -1:
        for i in range(n):
            dp[i][0] = -1
        for i in range(m):
            dp[0][i] = -1
    else:
        dp[0][0] = 1
        for i in range(1, n):
            if dp[i][0] != -1:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, m):
            if dp[0][i] != -1:
                dp[0][i] = dp[0][i - 1]

    # 2중 반복문으로 dp배열 갱신 (위쪽, 왼쪽에 연못 있을경우 예외 위주로)
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                continue
            elif dp[i - 1][j] == -1 and dp[i][j - 1] == -1:
                dp[i][j] = -1
            elif dp[i][j - 1] == -1:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j] == -1:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    # dp[-1][-1] 값이 -1이면 도달 불가능 -> -1이 아니라 0 return
    return dp[-1][-1] if dp[-1][-1] != -1 else 0