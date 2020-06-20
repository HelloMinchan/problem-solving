def solution(clothes):
    hashClothes = dict()
    
    for _, kind in clothes:
        hashClothes[kind] = hashClothes.get(kind, 0) + 1
    
    combi = 1
    for num in hashClothes.values():
        combi *= num + 1
    
    return combi - 1
