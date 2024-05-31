from itertools import combinations
# 각 주문에 대해 조합을 생성하여 해시 맵에 추가

def solution(orders, course):
    # 조합 길이별 해시맵 선언
    hashmap = [{} for i in range(max(course)+1)]

    for order in orders:
        order = list(order)
        order.sort()
        for i in range(min(course),max(course)+1):
            combies = list(combinations(order,i))
            
            for combi in combies:
                if hashmap[i].get(combi) :
                    hashmap[i][combi] += 1
                else:
                    hashmap[i][combi] = 1

    ans = []
    for count in hashmap:
        if count == {}:
            continue

        newCount = list(count.items())
        newCount.sort(reverse=True,key = lambda x : x[1])
        maxCount = newCount[0][1]
        
        # 코스 배열에 포함되지 않는 조합의 갯수인지 체크
        if len(newCount[0][0]) not in course:
            continue
        
        # 조합의 갯수가 2개 이상인지 체크
        if newCount[0][1] < 2:
            continue
            
        for key,value in newCount:
            if value < maxCount:
                break
            invertList = [*key]
            invertList = ''.join(invertList)
            ans.append(invertList)
    
    ans = sorted(ans)    
        
    return ans