import math

def solution(fees, records):
    timesMaps = {}
    inAndOut = {}
    
    for record in records:
        time, carNum, sign = record.split()

        if sign == 'IN':
            inAndOut[carNum] = list(map(int,time.split(':')))
        else:
            inTime = inAndOut[carNum]
            outTime =list(map(int,time.split(':')))
            times = (outTime[0] - inTime[0]) * 60 + (outTime[1] - inTime[1])
            
            if timesMaps.get(carNum):
                timesMaps[carNum] += times
            else:
                timesMaps[carNum] = times
            inAndOut[carNum] = None
        
    
    for key, value in inAndOut.items():
        if value != None:
            inTime = value
            outTime = [23,59]
            times = (outTime[0] - inTime[0]) * 60 + (outTime[1] - inTime[1])
            
            if timesMaps.get(key):
                timesMaps[key] += times
            else:
                timesMaps[key] = times

    carNumArr = sorted(list(timesMaps))
    answer = []
    for i in carNumArr:
        if timesMaps[i] <= fees[0] :
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((timesMaps[i]-fees[0]) / fees[2]) * fees[3])

    return answer