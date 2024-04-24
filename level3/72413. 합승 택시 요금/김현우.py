import sys

INF = sys.maxsize


def solution(n, s, a, b, fares):
    answer = INF
    graph = [[INF for _ in range(n + 1)] for __ in range(n + 1)]

    # 그래프 초기화 (i 지점에서 j 지점까지 가는 경로)
    for i, j, cost in fares:
        graph[i][j] = cost
        graph[j][i] = cost

    # 그래프 초기화 (자기 자신으로 가는 경로 == 0)
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # s -> i 지점까지 가는 택시요금 (합승) + i 지점부터 각자 a, b 지점까지 가는 택시요금 최소값 갱신
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer