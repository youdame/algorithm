

def solution(cacheSize, cities):
    cache = []
    
    hit = 0
    miss = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:   
        city = city.lower()
        if city not in cache:
            # print("miss")
            miss += 1
            if cache and len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
        else:
            # print("hit")
            hit += 1
            cache.pop(cache.index(city))
            cache.append(city)
        # print(cache)
    return hit * 1 + miss * 5
            