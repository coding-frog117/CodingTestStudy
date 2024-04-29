def solution(want, number, discount):
    answer = 0

    # check_dic : 10일치 제품 체크용 딕셔너리
    # w_dic : 정현이가 원하는 제품 딕셔너리
    check_dic = {}
    w_dic = {want[i]: number[i] for i in range(len(want))}

    # check_dic 초기화
    for i in range(10):
        if discount[i] in check_dic.keys():
            check_dic[discount[i]] += 1
        else:
            check_dic[discount[i]] = 1

    # 10일 단위로 이동해가면서 w_dic이 check_dic 안에 들어가는지 체크
    for i in range(len(discount) - 10):

        is_satisfied = True
        for k, v in w_dic.items():
            if k not in check_dic.keys() or check_dic[k] != v:
                is_satisfied = False

        if is_satisfied:
            answer += 1

        check_dic[discount[i]] -= 1
        if discount[i + 10] in check_dic.keys():
            check_dic[discount[i + 10]] += 1
        else:
            check_dic[discount[i + 10]] = 1

    # 반복문에서 체크 못한 마지막 한번 체크
    is_satisfied = True
    for k, v in w_dic.items():
        if k not in check_dic.keys() or check_dic[k] != v:
            is_satisfied = False

    if is_satisfied:
        answer += 1

    return answer