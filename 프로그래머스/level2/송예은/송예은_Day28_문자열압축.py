import sys

def solution(s):    
    minCount = sys.maxsize
    for i in range(1,len(s)//2+2):
        count = 0
        currCount = 0
        checkStr = s[:i]
        newStr= ''
        for idx in range(0,len(s),i):
            currStr = s[idx:idx+i]
            
            if currStr == checkStr:
                currCount += 1
            else:
                if currCount >1:
                    newStr += (str(currCount)+checkStr)
                else:
                    newStr += checkStr
                checkStr = currStr
                currCount = 1
        if currCount > 1:
            newStr += (str(currCount)+checkStr)
        else:
            newStr += checkStr
        minCount = min(minCount,len(newStr))
    return minCount