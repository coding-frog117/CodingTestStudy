from collections import deque

def solution(order):
    container = deque()
    for i in range(1,len(order)+1):
        container.append(i)
    
    support = []
    answer = 0
    
    for i in order:
        if len(container) > 0 and container[0] == i:
            container.popleft()
            answer += 1
        elif len(support) > 0 and support[-1] == i:
            support.pop()
            answer += 1
        elif i > container[0] :
            while container[0] != i :
                num = container.popleft()
                support.append(num)
            container.popleft()
            answer += 1
        else:
            break
            
    return answer