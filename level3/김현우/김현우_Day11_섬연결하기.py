def solution(n, costs):
    # 최소 스패닝 트리 (MST) 구현 문제
    # 여기서는 크루스칼 알고리즘 사용
    answer = 0

    # 최소 비용순으로 오름차순 정렬 후, 모든 섬이 연결될때까지 비용이 낮은 순으로 연결
    costs.sort(key=lambda x: (x[2]))
    bridge = set([costs[0][0]])

    while len(bridge) != n:
        # 가장 작은 비용 도로부터 탐색
        for c in costs:
            # 이미 시작점과 끝점이 둘 다 bridge에 존재하면, 해당 다리는 이미 bridge에 존재함 -> 패스
            if c[0] in bridge and c[1] in bridge:
                continue

            # 시작점, 끝점 둘 다 bridge에 없으면 아직 체크하지 않음
            if c[0] not in bridge and c[1] not in bridge:
                continue

            # 위 두 조건을 제외하고 최소 비용 도로를 bridge 안에 넣은 후 재탐색
            bridge.add(c[0]);
            bridge.add(c[1])
            answer += c[2]
            break

    return answer