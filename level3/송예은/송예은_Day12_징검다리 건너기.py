import sys

def solution(stones, k):
    # k만큼 연속된 길이의 구간 구하기, 구간에서 가장 큰 값이 작은 구간 구하기
    answer = 0
    arr = stones[:k]
    maxCount = sys.maxsize
    
    for i in range(k,len(stones)):
        arr = stones.append(i)
        arr = arr[1:]
        maxCount = min(maxCount,max(arr))
        print(maxCount)
    return answer