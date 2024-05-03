def solution(cacheSize, cities):
    if cacheSize ==  0:
        return len(cities) * 5
    reference = {}
    answer = 0
    cache = []
    
    for city in cities:
        if city.lower() in cache:
            answer += 1
            cache.remove(city.lower())
            cache.insert(0,city.lower())
        
        else:
            if len(cache) == cacheSize:
                cache.pop()
            cache.insert(0,city.lower())
            answer += 5
            
    return answer