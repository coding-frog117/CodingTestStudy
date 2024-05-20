def solution(enroll, referral, seller, amount):
    # 문제 설명이 매우 복잡한데, 결국은 제일 자식노드부터 수익 90% 먹고
    # 남은 10%를 부모 노드로 올리는 식으로 구현하면 됨

    graph = {e: [] for e in enroll}
    profit = {e: 0 for e in enroll}

    # 말단 노드부터 부모 노드로 올라가며 탐색할 수 있도록 그래프 구현
    for i in range(len(enroll)):
        graph[enroll[i]].append(referral[i])

    # 문제에서 주어진 seller에 대해 탐색
    for i in range(len(seller)):
        cur_seller, p = seller[i], amount[i] * 100

        while True:
            if p == 0 or cur_seller == "-":
                break
            profit[cur_seller] += p - p // 10
            p = p // 10
            cur_seller = graph[cur_seller][0]

    ans = [profit[enroll[i]] for i in range(len(enroll))]

    return ans