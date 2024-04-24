def solution(n):
    arr =[[],[],[]]
    for i in range(1,n+1):
        arr[0].append(i)
    count =0
    
# 규칙 찾기 시도함 ->실패..

# top에 위치한 원판이 1번의 top보다 크면 2,3번을 옮겨주기
    if arr[1][-1] > arr[0][-1] and arr[2][-1] > arr[0][-1] :
            arr[0].append(min(arr[1][-1],arr[0][-1]))
            
    
    return answer