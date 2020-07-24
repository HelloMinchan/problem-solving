import sys
input = sys.stdin.readline

trash = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "b", "w", "x", "y", "z"]
t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    isFirst = True
    answer = []
    index = 0
    
    for i in range(n):
        ix = 0
        temp = ""

        if a[i] == 0:
            while trash[ix] in answer:
                ix += 1

                if ix >= 25:
                    ix = 0

            answer.append(trash[ix])
                
        else:
            if isFirst:
                isFirst = False
                answer.append(words[a[i]] + chr(ord('a') + index))
                index += 1
                if index >= 26:
                    index = 0
                answer.append(words[50] + chr(ord('a') + index))
                index += 1
                if index >= 26:
                    index = 0
            else:
                while words[a[i]] + chr(ord('a') + index) in answer:
                    index += 1
                    if index >= 26:
                        index = 0
                answer.append(words[a[i]] + chr(ord('a') + index))

    print(answer)
