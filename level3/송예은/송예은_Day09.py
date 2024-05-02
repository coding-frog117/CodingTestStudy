def solution(genres, plays):
    hashmap = {}
    
    for i in range(len(genres)):
        if hashmap.get(genres[i]):
            hashmap[genres[i]].append([plays[i],i])
        else:
            hashmap[genres[i]] = [[plays[i],i]]
    arr = []
    for values in hashmap.values():
        values.sort(reverse=True)
        arr.append(values)
    arr.sort(reverse=True)
    
    for i in arr:
        for j in range(len(arr[i])):
            if j > 1:
                break
            answer.append(arr[i][j])