from collections import deque


def solution(cacheSize, cities):
    # 결국 LRU 알고리즘 구현하는 문제
    count = 0
    cache = deque()

    for city in cities:
        city = city.lower()
        # Cache hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            count += 1
        # Cache miss
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            elif len(cache) == cacheSize:
                cache.append(city)
                cache.popleft()
            count += 5
    return count