import math

def solution(n, words):
    answer = []
    currNum = 0
    prevWord = words[0][0]
    seen = []
    
    for i in range(len(words)):
        currNum = currNum+1
        if currNum > n:
            currNum = 1
         
        currword = words[i]
        if prevWord[-1] != currword[0] or currword in seen:
            return [currNum,math.ceil((i+1)/n)]
        
        prevWord = currword
        seen.append(prevWord)
        
    return [0,0]