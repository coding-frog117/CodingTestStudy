def solution(picks, minerals):
    power = [[1,1,1],[5,1,1],[25,5,1]]
    pickName = {'diamond' : 0, 'iron' : 1, 'stone' : 2}
    answer = 0
    minerals.reverse()
    # 다이아 -> 철 -> 돌 곡괭이 순서대로 사용하는 것이 유리함. 따라서 순차적으로 순회
    for i in range(len(picks)):
        if len(minerals) == 0:
            return answer
        
        if picks[i] == 0:
            continue
        
#       해당 광물 갯수만큼 5번씩 캐기
        for z in range(picks[i]):
            pickNum = i
            for j in range(5):
                crntMineralNum = pickName[minerals[-1]]
                powerNum = power[pickNum][crntMineralNum]
                answer += powerNum
            
                minerals.pop()
                if (len(minerals) ==0):
                    return answer
    return answer