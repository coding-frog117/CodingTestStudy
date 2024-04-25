def solution(A, B):
    answer = 0

    # A의 출전순서가 정해졌더라도 거기에 맞춰서 B 출전순서를 맞추면 됨
    # -> A, B 둘 다 정렬해버려도 상관없음
    A.sort(reverse=True);B.sort(reverse=True)
    index = 0

    # 숫자가 높은 사람들끼리 붙이는 게 더 이득 <- 증명필요?
    # A, B 둘 다 숫자가 높은 순서대로 까면서 B가 높을 경우만 카운트
    for i in range(len(B)):
        if A[i] < B[index]:
            answer += 1
            index += 1

    return answer