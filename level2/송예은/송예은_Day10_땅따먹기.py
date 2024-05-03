def solution(land):
    #DFS로 모든 경로 탐색해서 최대값 return
    #자기자신의 인덱스만 제외하고 선택하기
    #시간초과뜸..
    
    answer = 0
    stack=[]
    
    for j in range(4):
        stack.append([0,j,land[0][j]])
    
    while stack:
        row,index,currSum = stack.pop()
        
        if row+1 >= len(land):
            answer = max(answer,currSum)
            continue
        
        for i in range(4):
            if index == i:
                continue
            stack.append([row+1,i,currSum+land[row+1][i]])

    return answer