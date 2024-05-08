def solution(s):
    answer = 0
    
    start = 0
    end = len(s)-1
    
    for i in range(len(s)):
        answer = max(leftCheck(s,i,end),rightCheck(s,i,end),answer)
    return answer
            
def leftCheck(s,start,end):
    length = 0
    while start<end:
        if s[start] == s[end]:
            if length ==0 :
                length = end-start+1
            start += 1
            end -=1
        else:
            end -=1
            length =0
    return length
                        
def rightCheck(s,start,end):
    length = 0
    while start<end:
        if s[start] == s[end]:
            if length ==0 :
                length = end-start+1
            start += 1
            end -=1
        else:
            start+=1
            length =0
    return length