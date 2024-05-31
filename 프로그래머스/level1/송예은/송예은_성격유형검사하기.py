# 각 유형 별 점수를 담은 score 변수 설정
# 돌면서 1~3 의 값이면 앞문자에 가중치를, 5~7의 값이면 뒷문자에 가중치를 기입
# 결과 중 점수가 큰 유형을 선택, 같다면 정렬 후 앞 유형 선택

answerScore = {1:3,2:2,3:1,5:1,6:2,7:3}
scores = {'R':[0,0],'T':[0,0],'C':[1,0],'F':[1,0],'J':[2,0],'M':[2,0],'A':[3,0],'N':[3,0]}

def solution(survey, choices):
    answer = ''
    for i in range(len(survey)):
        # 답변이 1,2,3일 경우 앞문자에 가중치 부여
        if choices[i] in [1,2,3]:
            targetType = survey[i][0]
            score = answerScore[choices[i]]
            scores[targetType][1] += score
        elif choices[i] in [5,6,7]:
            targetType = survey[i][1]
            score = answerScore[choices[i]]
            scores[targetType][1] += score
    
    value = list(scores.items())
    value.sort(key = lambda x: (x[1],-ord(x[0])))
    
    for i in range(1,len(value),2):
        answer += value[i][0]
        
    return answer