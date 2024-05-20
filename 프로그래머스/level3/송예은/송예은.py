def solution(routes):
    routes.sort()
    start = routes[0][0]
    end = routes[0][1]
    answer = 0
    
    for i in range(1,len(routes)):
        if (routes[i][0] > end):
            answer += 1
            start = routes[i][0]
            end = routes[i][1]
            continue
        
        if (routes[i][0] > start):
            start = routes[i][0]
            
        if (routes[i][1] < end):
            end = routes[i][1]
            
    answer += 1
    return answer