# 기존 코드의 문제 : 곡괭이를 효율적으로 사용할 수 있는 방법을 고려하지 않고 무조건 순차적으로 사용함
# 개선 : 그룹별로 묶어서 많이 쓰이는 순서대로(다이아 -> 철 -> 돌) 정렬, 이후 맞춰서 다이아부터 순차 적용
# 문제점 : 코드가 지저분함. 구현 역량 향상 필요할듯..

def solution(picks, minerals):
    power = [[1,1,1],[5,1,1],[25,5,1]]
    pickName = {'diamond' : 0, 'iron' : 1, 'stone' : 2}
    answer = 0

    # 캘 수 있는 광물 수보다 len(minerals)가 크면 캘 수 있는 광물 수만큼 자름
    totalPicks = 0
    for pick in picks:
        totalPicks += pick*5
        
    if (totalPicks < len(minerals)):
        minerals = minerals[0:totalPicks]

    # 현재 광물을 다섯개씩 나눠 그룹으로 생성 , 광물 종류별로 기록
    groupLength = len(minerals) // 5
    if (len(minerals) % 5) :
        groupLength += 1
        
    mineralCount = [[0,0,0] for _ in range(groupLength)]
    count = 0
    index = 0
    
    for mineral in minerals:
        if (count >= 5):
            count = 0
            index += 1
            
        mineralCount[index][pickName[mineral]] += 1
        count += 1
        
    #다이아 -> 철 -> 돌 많은 순서대로 정렬
    mineralCount.sort(reverse=True)
    
    # 광물 카운팅 한 것을 순차대로 answer 에 더하기
    for pick in range(groupLength):
#          곡괭이 종류에 맞는 피로도 더하기
        if (picks[0] != 0):
            picks[0] -= 1
            for i in range(3):
                answer += power[0][i]*mineralCount[pick][i]
                
        elif (picks[1] != 0):
            picks[1] -= 1
            for i in range(3):
                answer += power[1][i]*mineralCount[pick][i]
                
        elif (picks[2] != 0):
            picks[2] -= 1
            for i in range(3):
                 answer += power[2][i]*mineralCount[pick][i]
               
    return answer