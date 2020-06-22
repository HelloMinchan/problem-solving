def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    charSet1 = []
    charSet2 = []
    
    for i in range(len(str1) - 1):
        if (str1[i] + str1[i + 1]).isalpha():
            charSet1.append(str1[i] + str1[i + 1])
    
    for i in range(len(str2) - 1):
        if (str2[i] + str2[i + 1]).isalpha():
            charSet2.append(str2[i] + str2[i + 1])
    
    plusSetLength = len(charSet1) + len(charSet2)
    sameSetLength = 0
    
    for cmpStr in charSet2:
        if cmpStr in charSet1:
            charSet1.remove(cmpStr)
            sameSetLength += 1
            
    if not plusSetLength:
        return 65536
    else:
        return int(sameSetLength / (plusSetLength - sameSetLength) * 65536)
