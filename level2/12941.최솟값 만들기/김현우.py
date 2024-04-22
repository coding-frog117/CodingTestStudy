def solution(A, B):
    answer = 0

    # 아이디어
    # 작은수*작은수 + 큰수*큰수 => 큰 수에 큰 수를 곱하면 숫자가 기하급수적으로 커짐
    # 즉, 작은수*큰수 + 큰수*작은수 형태가 유지되도록 곱해감
    # => 한 배열은 오름차순 정렬, 나머지 배열은 내림차순 정렬 후 각각 곱함
    A.sort(); B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer