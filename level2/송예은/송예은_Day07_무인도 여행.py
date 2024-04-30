def solution(maps):
    stack = []
    seen = []
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        
    isInitialize = False
    for i in range(len(maps)):
        if isInitialize == True:
            break
        for j in range(len(maps[0])):
            if maps[i][j] != "X":
                stack.append([i,j,int(maps[i][j])])
                seen.append([i,j])
                isInitialize = True
                break
    if len(stack) == 0:
        return [-1]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    answer = []
    
    while stack:
        y,x,count = stack.pop()
        seen.append([y,x])
        isPossible = False
        print(y,x,count)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(maps[0]) or ny >= len(maps):
                continue
            if [ny,nx] in seen:
                continue
            if maps[ny][nx] == 'X':
                continue

            stack.append([ny,nx,int(count)+int(maps[ny][nx])])
            isPossible = True
            
        if isPossible == False:
            answer.append(count)
        
    return answer