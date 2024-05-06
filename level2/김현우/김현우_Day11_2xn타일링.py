def solution(n):
    # DP 웰노운 문제
    # 점화식은 결국 피보나치 수열임
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[-1]