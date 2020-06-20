def solution(phone_book):
    hashNum = dict()
    
    for num in phone_book:
        hashNum[num] = 1
    
    for num in phone_book:
        temp = ""
        for n in num:
            temp += n
            if temp in hashNum and temp != num:
                return False
    
    return True
