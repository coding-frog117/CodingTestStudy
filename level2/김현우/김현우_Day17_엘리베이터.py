from collections import deque, defaultdict
import sys


def solution(storey):
    # BFS 탐색으로 구해야 되는데, 10^C 형태의 탐색길이를 어떻게 처리하냐가 관건

    q = deque()
    q.append([0, 0, storey])
    ans = sys.maxsize

    while q:
        depth, count, num = q.popleft()
        str_num = str(num)

        # 현재 층수가 n*10^C 형태일 때 예외처리
        if depth == len(str_num) - 1:
            plus = int(str_num[0])
            ans = min(ans, count + plus)
            ans = min(ans, count + 11 - plus)
            continue

        # depth(자리수)를 하나씩 올려가면서 계산
        unit = 10 ** depth
        digit = int(str_num[len(str_num) - 1 - depth])
        q.append([depth + 1, count + digit, num - digit * unit])
        q.append([depth + 1, count + 10 - digit, num + (10 - digit) * unit])

    return ans