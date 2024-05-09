import heapq
import sys

INF = sys.maxsize


# 다익스트라 템플릿문제
def solution(n, roads, sources, destination):
    # 문제에서 주어진 roads를 graph로 초기화
    graph = {x: {} for x in range(1, n + 1)}
    for r in roads:
        s, e = r
        graph[s][e] = 1
        graph[e][s] = 1

    # 다익스트라 최단거리 계산용 dist 선언
    dist = {node: INF for node in graph}
    dist[destination] = 0

    # 시작점을 destination으로 잡고 이하 다익스트라 알고리즘 구현체
    queue = []
    heapq.heappush(queue, [dist[destination], destination])

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if dist[current_node] < current_dist:
            continue

        for edge, weight in graph[current_node].items():
            distance = current_dist + weight

            if distance < dist[edge]:
                dist[edge] = distance
                heapq.heappush(queue, [distance, edge])

    # dist에서 초기값 INF가 남아있다면 왕복불가 -> -1로 바꾸고 나머지는 최단거리값으로 바꾸기
    answer = [dist[s] if dist[s] != INF else -1 for s in sources]

    return answer