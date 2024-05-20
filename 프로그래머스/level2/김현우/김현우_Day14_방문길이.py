def solution(dirs):
    dif = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}  # URDL -> 이동칸수로 치환
    p = set()  # 처음 걸어본 길 리스트
    pos = (0, 0)  # 현재 위치

    for d in dirs:
        # 명령에 따라 이동후 위치 계산
        pos_x, pos_y = pos
        dx, dy = dif[d]
        nx, ny = pos_x + dx, pos_y + dy

        # 이동 후 위치가 grid 범위 밖일 경우 명령 무시
        if not (-5 <= nx <= 5) or not (-5 <= ny <= 5):
            continue

        # 경로 이동 순방향, 역방향을 모두 체크하기 위에 둘 다 넣음
        p.add((pos_x, pos_y, nx, ny))
        p.add((nx, ny, pos_x, pos_y))

        # 현재위치 갱신
        pos = (nx, ny)

    # 경로를 넣을 때 순방향, 역방향 둘 다 체크했으므로 마지막에 2로 나눔
    return len(p) // 2