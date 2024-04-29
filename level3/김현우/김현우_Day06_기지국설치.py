import math


def solution(n, stations, w):
    answer = 0

    # 먼저 distances 리스트에 전파 안터지는 구간 길이를 전부 저장
    distances = []

    # 시작 지점부터 첫번째 기지국까지 길이
    if stations[0] - w - 1 > 0:
        distances.append(stations[0] - w - 1)

    # 마지막 기지국부터 끝 지점까지 길이
    if n - stations[-1] - w > 0:
        distances.append(n - stations[-1] - w)

    # 기지국들 사이의 길이
    for i in range(len(stations) - 1):
        if stations[i + 1] - stations[i] - 2 * w - 1 > 0:
            distances.append(stations[i + 1] - stations[i] - 2 * w - 1)

    # 기지국 전파가 닿지 않는 길이 d 안에 설치해야 되는 최소 기지국 수
    # = d / (2*w + 1) <- 기지국 하나가 퍼트릴 수 있는 전파 최대길이는 2*w + 1
    for d in distances:
        answer += math.ceil(d / (2 * w + 1))

    return answer