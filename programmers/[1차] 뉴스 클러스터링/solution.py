from collections import defaultdict

MULTI_VALUE = 65536

def solution(str1, str2):
    multi_set1 = defaultdict(int)
    multi_set2 = defaultdict(int)
    
    for i in range(len(str1) - 1):
        word = (str1[i] + str1[i+1]).upper()
        if word.isalpha():
            multi_set1[word] += 1
    
    for i in range(len(str2) - 1):
        word = (str2[i] + str2[i+1]).upper()
        if word.isalpha():
            multi_set2[word] += 1
            
    intersection = []
    for word, count in multi_set1.items():
        if multi_set2.get(word, 0):
            for _ in range(min(multi_set2.get(word, 0), count)):
                intersection.append(word)
    
    union = []
    intersection_count = 0
    for word, count in multi_set1.items():
        for _ in range(count):
            union.append(word)
    
    for word, count in multi_set2.items():
        for _ in range(count):
            union.append(word)
    
    if union:
        return int(len(intersection) / (len(union) - len(intersection)) * MULTI_VALUE)
    else:
        if intersection:
            return 0
        else:
            return MULTI_VALUE
        