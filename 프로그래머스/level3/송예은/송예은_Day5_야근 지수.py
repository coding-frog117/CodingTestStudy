def solution(n, works):
    answer = 0
    count = 0
    index = 0
    works.sort(reverse=True)
    
    while count < n:
        while index < len(works)-1:
            if works[index] > works[index+1] :
                works[index] -= 1
                count += 1
                if count == n :
                    break
            else :
                index+= 1

    for work in works:
        answer += work * work
        
    return answer