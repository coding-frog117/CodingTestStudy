def solution(m, n, puddles):
        
    # 최소 경로 카운트할 배열 설정
    count = [[0]*m for i in range(n)]
    count[0][0] = 0
    if (m>1):
        count[0][1] = 1
    if (n>1):
        count[1][0] = 1
        
    #웅덩이 위치 입력
    for puddle in puddles:
        count[puddle[1]-1][puddle[0]-1] = -1
    
    for i in range(0, n):
        for j in range(0, m):
            if count[i][j] == -1 or count[i][j] != 0 :
                continue
            
            # 바로 위쪽, 왼쪽 인덱스까지의 최솟값 구하기
            dx = count[i][j-1]
            dy = count[i-1][j]
            
            if (dx == -1 and dy != -1):
                count[i][j] = dy
            elif (dy == -1 and dx != -1):
                count[i][j] = dx
            elif (dy == -1 and dx == -1):
                count[i][j] = -1
            else:
                count[i][j] = dx+dy
        
    if (count[n-1][m-1] == -1):
        return 0
    answer = (count[n-1][m-1]) % 1000000007
    return answer