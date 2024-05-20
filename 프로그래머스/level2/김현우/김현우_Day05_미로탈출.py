from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(maps):
    # 결국 S -> L, L -> E 두 구간에서 BFS 두번 돌리면 됨

    len_x, len_y = len(maps), len(maps[0])
    ans = 0
    is_reachable_L, is_reachable_E = False, False  # S -> L, L -> E 구간이 막혀있는지 뚫려있는지 체크

    # S -> L 구간 BFS
    visited = [[False for _ in range(len_y)] for __ in range(len_x)]
    q = deque()
    d = None

    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j] == 'S':
                q.append((i, j, 0))
                visited[i][j] = True
            elif maps[i][j] == 'L':
                d = (i, j)

    while q:
        x, y, count = q.popleft()

        if d == (x, y):
            ans += count
            is_reachable_L = True
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len_x and 0 <= ny < len_y:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    q.append((nx, ny, count + 1))
                    visited[nx][ny] = True

    # L -> E 구간 BFS
    visited = [[False for _ in range(len_y)] for __ in range(len_x)]
    q = deque()
    d = None

    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j] == 'L':
                q.append((i, j, 0))
                visited[i][j] = True
            elif maps[i][j] == 'E':
                d = (i, j)

    while q:
        x, y, count = q.popleft()

        if d == (x, y):
            ans += count
            is_reachable_E = True
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len_x and 0 <= ny < len_y:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    q.append((nx, ny, count + 1))
                    visited[nx][ny] = True

    # S -> L, L -> E 둘 다 도달 가능하면 ans값 리턴, 아니면 -1 리턴
    return ans if is_reachable_L and is_reachable_E else -1