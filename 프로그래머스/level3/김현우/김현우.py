import sys


def solution(routes):
    answer = 0

    # 아이디어 : 자동차가 제일 많이 겹치는 구간을 우선적으로 체크해 나감
    # 진출 지점 기준으로 정렬 후, 자동차가 빠져나갈 때마다 카메라를 추가
    # 유사 문제 : 백준 1931, 백준 11000
    routes.sort(key=lambda x: x[1])
    pos = -sys.maxsize

    for r in routes:
        if pos < r[0]:
            answer += 1
            pos = r[1]

    return answer