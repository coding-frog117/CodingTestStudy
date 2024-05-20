from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)

    # DFS로 풀기

    # 그래프 초기화
    for a, b in tickets:
        graph[a].append(b)

    # 알파벳 순서에 맞게 탐색하도록 정렬
    for key, _ in graph.items():
        graph[key].sort()

    # DFS 탐색 구현
    def dfs(s):
        while graph[s]:
            dfs(graph[s].pop(0))

        # 도착점에 도착했을 경우 해당 도착지 append
        if not graph[s]:
            answer.append(s)
            return

    dfs("ICN")

    # DFS 탐색후 최후 도착지부터 역순으로 저장되므로, 그 역순을 출력하면 경로를 얻을 수 있음
    return answer[::-1]