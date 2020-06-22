def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5
    
    answer = 0
    
    cache = []
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop()
            answer += 5
        
        cache.insert(0, city)
    
    return answer
