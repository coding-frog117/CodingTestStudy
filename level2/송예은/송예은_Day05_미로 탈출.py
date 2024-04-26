def DP(start,end,maps):
    maps[start[0]][start[1]] = 0
    
    for i in range(end[0]-start[0]):
        for j in range(end[1]-start[1]):
            
            # 오른쪽 ,아래 방향으로 이동
            # 비용 작은 것 고르기
            if end[1] > start[1] :
                if i-1 < 0 or maps[i-1][j] == 'X':
                    maps[i][j] = maps[i][j-1] + 1
                elif j-1 < 0 or maps[i][j-1] == 'X':
                    maps[i][j] = maps[i-1][j] + 1
                else:
                     maps[i][j] = min(maps[i-1][j],maps[i][j-1])+1
            # 왼쪽, 아래 방향으로 이동
            else:
                if i-1 < 0 or maps[i-1][j] == 'X':
                    maps[i][j] = maps[i][j+1] + 1
                elif j+1 < 0 or maps[i][j+1] == 'X':
                    maps[i][j] = maps[i-1][j] + 1
                else:                
                    maps[i][j] = min(maps[i-1][j],maps[i][j+1])+1

def solution(maps):
    answer = 0
    S = []
    L = []
    start = []
    end = []
    
    # S,L좌표구하기
    for y in range(len(maps)):
        if x in range(len(maps)): 
            if S != [] and L != []:
                break
            if maps[y][x] == 'S':
                S = [y,x]
            elif maps[y][x] == 'L':
                L = [y,x]
            
        start_y , start_x = S
        lebber_y, lebber_x = L
        
        if (start_x == lebber_x):
            answer += abs(lebber_y - start_y)
        elif (start_y == start_y):
            answer += abs(lebber_x - start_x)
        else:
            if S[0] > L[0] :
                start = L
                end = S
            else:
                start = S
                end = L
        
        maps[start[0]][start[1]+1] = 1
        maps[start[1]][start[0]+1] = 1
    return answer