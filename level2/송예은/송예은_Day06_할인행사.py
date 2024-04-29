def solution(want, number, discount):
    for i in range(len(want)):
        want[i] = [want[i],number[i]]
        
    want.sort()
    disIdx = 0
    answer = 0
    
    #sub 배열 체크 -> 시간 초과됨
    for disIdx in range(len(discount)):
        subArr = discount[disIdx : disIdx+11] if (disIdx+11 <= len(discount)) else discount[disIdx: len(discount)]
        
        print(subArr)
        
        subArr.sort()
        wantIdx = 0
        subIdx = 0
        newWant = want[:]
        print(newWant)
        if sum(number) > len(subArr):
            break
        
        while subIdx < len(subArr):
            if subArr[subIdx] == newWant[wantIdx][0]:
                newWant[wantIdx][1] -= 1
            else:
                subIdx += 1
            
            if newWant[wantIdx][1] == 0:
                answer += 1
                wantIdx += 1
                if wantIdx >= len(newWant):
                    break
    
    return answer