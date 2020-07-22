import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input().rstrip())
    b = list(input().rstrip())

    answer = []
    while a != b:
        temp = []
        isWrong = False
        count = 0

        for i in range(n):
            if a[i] == '1':
                temp.append('0')
            else:
                temp.append('1')
                
            if a[i] != b[i]:
                isWrong = True
                count += 1
                if answer and count == answer[-1]:
                    continue
                break
            else:
                count += 1
        
        if isWrong:
            answer.append(count)
            a = list(reversed(temp)) + a[count:]
    
    if len(answer):
        print(len(answer), *answer)
    else:
        print(0)
