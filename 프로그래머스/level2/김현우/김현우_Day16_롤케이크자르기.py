def solution(topping):
    answer = 0

    # 딕셔너리(hashmap)를 이용
    # count_l : 철수, count_r : 동생
    count_l = {}
    count_r = {}
    # 초기 위치(인덱스 0) 시점 동생 케이크 초기화
    for n in topping:
        if n in count_r:
            count_r[n] += 1
        else:
            count_r[n] = 1

    # 인덱스 움직여가면서 토핑 개수 확인
    for n in topping:
        # 개수 같으면 카운트
        if len(count_l) == len(count_r):
            answer += 1

        # 철수 케이크 갱신
        if n in count_l:
            count_l[n] += 1
        else:
            count_l[n] = 1

        # 동생 케이크 갱신
        count_r[n] -= 1
        if count_r[n] == 0:
            del count_r[n]

    return answer