def solution(n):
    count = [0 for _ in range(n+1)]
    count[1] = 1
    count[2] = 2
    
    for i in range(3,n+1):
        count[i] = (count[i-1] + count[i-2])% 1000000007

    return count[n]