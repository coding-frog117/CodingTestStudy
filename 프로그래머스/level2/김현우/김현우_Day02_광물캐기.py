def solution(picks, minerals):
    answer = 0

    # 예외처리
    # [0, 0, 1], ["stone", "stone", "stone", "stone", "stone", "diamond"] 와 같은 경우
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]

    # 햇갈리니까 우선 광석 종류를 숫자로 변환
    d = {"diamond": 1, "iron": 2, "stone": 3}
    minerals = [d[m] for m in minerals]

    # 광석을 5개 단위로 쪼개기
    # [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], ...]
    m = [minerals[5 * i:5 * i + 5] for i in range(len(minerals) // 5 + 1)]

    # 위에서 만든 5개 광석 단위에 종류별로 광석이 몇개씩 있는지 카운트
    # [[5, 0, 0], [0, 5, 0], ...]
    count = [[0] * 3 for _ in range(len(m))]
    for i in range(len(m)):
        for num in m[i]:
            count[i][num - 1] += 1

    # 카운트 정렬 -> 이렇게 되면 각 단위별로 [다이아, 철, 돌] 내림차순으로 정렬
    # [[5, 0, 0], [0, 5, 0], ...]
    count.sort(reverse=True)

    # picks도 계산에 용이하게 변환
    p = [[1, 1, 1] for _ in range(picks[0])] + [[5, 1, 1] for _ in range(picks[1])] + [[25, 5, 1] for _ in
                                                                                       range(picks[2])]

    # answer 계산
    for i in range(min(len(p), len(count))):
        for j in range(3):
            answer += count[i][j] * p[i][j]

    return answer