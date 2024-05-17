def solution(sequence):
    pulse = lambda x: 1 if x % 2 == 0 else -1
    # 1로 시작하는 펄스, -1로 시작하는 펄스 구분
    pulse_plus = [sequence[i] * pulse(i) for i in range(len(sequence))]
    pulse_minus = [-sequence[i] * pulse(i) for i in range(len(sequence))]

    # dp[i][j] : i번째 원소를 마지막 원소로 하는 경우 펄스 부분수열 최대값
    # j가 0일 때 pulse_plus, 1일 때 pulse_minus
    dp = [[0] * 2 for _ in range(len(sequence))]
    dp[0] = [sequence[0], sequence[0]]

    for i in range(len(sequence)):
        dp[i][0] = max(pulse_plus[i], pulse_plus[i] + dp[i - 1][0])
        dp[i][1] = max(pulse_minus[i], pulse_minus[i] + dp[i - 1][1])

    # 구해진 모든 경우의 수에서 최대값 뽑아내기
    return max(map(max, dp))