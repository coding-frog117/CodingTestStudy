from heapq import *


def solution(n, works):
    # 제곱수를 줄이기 위해, 일의 양이 많은 순서대로 해나가야 됨
    # -> 우선순위 큐 사용

    # 야근으로 일을 다 끝낼 수 있으면 피로도 0
    if sum(works) <= n:
        return 0

    # works 배열을 최대 힙으로 변환
    works = [-w for w in works]
    heapify(works)

    # n시간 야근하면서 남은 일이 가장 많은 것부터 순차적으로 해나감
    while n:
        w = heappop(works)
        w += 1;
        n -= 1
        heappush(works, w)

    return sum([w ** 2 for w in works])