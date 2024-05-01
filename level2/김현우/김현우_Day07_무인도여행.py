from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(maps):
    # BFS 탐색을 하면서 섬 덩어리를 찾기 -> 섬에 있는 모든 식량 더해서 answer에 append
    r, c = len(maps), len(maps[0])
    visited = [[False for _ in range(c)] for __ in range(r)]

    answer = []

    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                temp = 0
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    temp += int(maps[x][y])

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'X' and not visited[nx][ny]:
                            q.append((nx, ny))

                answer.append(temp)

    return sorted(answer) if answer else [-1]