def findLength(num,target):
    y,x = num
    target_y,target_x = target
    
    return abs(y-target_y)+abs(x-target_x)

left = [1,4,7,'*']
right = [3,6,9,'#']

mapsSet = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],'*':[3,0],0:[3,1],'#':[3,2]}

def solution(numbers, hand):
    currLeft = [3,0]
    currRight = [3,2]

    answer = ''
    for i in numbers:
        if i in left:
            answer += 'L'
            currLeft = mapsSet[i]
        elif i in right :
            answer += 'R'
            currRight = mapsSet[i]
        else :
            leftLength = findLength(currLeft,mapsSet[i])
            rightLength = findLength(currRight,mapsSet[i])
            if leftLength > rightLength :
                answer += 'R'
                currRight = mapsSet[i]
            elif leftLength < rightLength :
                answer += 'L'
                currLeft = mapsSet[i]
            else:
                if hand== 'left':                
                    answer += 'L'
                    currLeft = mapsSet[i]
                else:
                    answer += 'R'
                    currRight = mapsSet[i]
                
    return answer