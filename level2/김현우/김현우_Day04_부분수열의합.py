def solution(sequence, k):
    # 부분수열 합이 k인 리스트를 담을 임시 리스트
    ans = []

    # 투포인터 시작 인덱스, 끝 인덱스, 부분수열합
    s, e, sum_k = 0, 0, sequence[0]
    while s < len(sequence):

        # 부분수열 합이 k이면 ans에 append
        if sum_k == k:
            ans.append([e - s, s, e])
            if e == len(sequence) - 1:
                sum_k -= sequence[s]
                s += 1
            else:
                e += 1
                sum_k += sequence[e]

        # 부분수열 합이 k가 아닐 시 투포인터 인덱스와 부분합 처리
        elif e == len(sequence) - 1 or sum_k > k:
            sum_k -= sequence[s]
            s += 1
        elif sum_k < k:
            e += 1
            sum_k += sequence[e]

    # 문제 조건에 맞는 부분수열을 솎아내기 위한 정렬
    ans.sort()

    return [ans[0][1], ans[0][2]]